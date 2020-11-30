"""
Chatbot for Twitch
"""


import os
import logging
import time
import functools
import inspect
from dataclasses import dataclass

from irc import *
from chatbot import Chatbot


class TwitchBot(Chatbot):
	"""
	Chat bot base class made specifically for Twitch

	In derived classes, commands handlers (responding to '!<command>' messages) are registered using the `@TwitchBot.new_command` decorator and must be methods that take a `Chatbot.Command` as parameter (along with self). The method name is used as command name and is not case-sensitive. The method docstring is used as help text if user types !help <command>. The name of the command (preceded or not by !) can be ommitted and will be inserted automatically.

	Example: 
	.. code-block:: python
		class SomeBot(TwitchBot):
			@TwitchBot.new_command
			def my_command(self, cmd: Chatbot.Command):
				'''{some_required_param} [some_optional_param]'''
				# Do something

	In this case, the command is activated by the message !my_command followed or not by something.
	!help my_command will send the help string (so '!my_command {some_required_param} [some_optional_param]').
	Note that the !my_command was inserted automatically.

	If a command callback is registered manually with `register_command`, it must only take one argument which is a `Chatbot.Command` (already be bound to self in case of a method).
	"""

	@classmethod
	def new_command(cls, fn):
		fn.is_command_function = True
		return fn

	twitch_chat_url = "irc.chat.twitch.tv"
	twitch_chat_port = 6697
	twitch_text_len_max = 500
	help_command_names = ("commands", "help")

	def __init__(self, logs_folder, log_to_console=True, pokemon_exception_handling=False):
		super().__init__(command_char="!")
		self.logs_folder = logs_folder
		self.log_to_console = log_to_console
		self.pokemon_exception_handling=pokemon_exception_handling
		self._setup_commands()

	def connect_and_join(self, password, nickname, channel):
		self.nickname = nickname
		self.channel = channel

		self.setup_logging(self.logs_folder, f"TwitchBot.{self.channel}.{self.nickname}", True)

		self.connect(TwitchBot.twitch_chat_url, TwitchBot.twitch_chat_port, True)

		self.authenticate(password, nickname)
		while self.receive_msgs() == []:
			pass

		# Membership (Twitch verbosity stuff)
		membership_requests = (
			"membership",
			#"tags",
			"commands"
		)
		for req in membership_requests:
			self.send("CAP", f"REQ :twitch.tv/{req}")
			while self.receive_msgs() == []:
				pass
			self.receive_msgs()

		self.join_channel(channel)
		while self.receive_msgs() == []:
			pass

		self.logger.debug("Done connecting.")

	def run(self):
		self.logger.debug("Listening to chat for commands...")
		while True:
			time.sleep(0.010) # Just to yield control of the thread
			try:
				msgs = self.receive_msgs()
				for msg in msgs:
					if msg.command == "PING":
						self.send("PONG", msg.params)
					elif msg.command == "PRIVMSG":
						privmsg = Privmsg.from_irc_msg(msg)
						if privmsg.channel == self.channel:
							self.dispatch_command(privmsg)
			except ConnectionError as e:
				self.logger.error(str(e))
				break
			except Exception as e:
				self.logger.error(f"{type(e).__name__}: {str(e)}")
				if not self.pokemon_exception_handling:
					break
			except:
				self.logger.error("Unknown exception caught")
				break
		
		ch = self.channel
		self.leave_channel()
		self.logger.debug(f"Left channel {ch}")
		self.irc_client.disconnect()
		self.logger.debug(f"Disconnected")

	def send_supported_commands(self, cmd: Chatbot.Command):
		if cmd.params is None:
			msg = "I can do all this: "
			msg += ", ".join(["!" + name for name in self.command_methods.keys()])
			self.send_privmsg(msg)
			help_commands_list = " or ".join(["!" + e for e in TwitchBot.help_command_names])
			self.send_privmsg(f"Sending {help_commands_list} followed by a command gives usage detail.")
		else:
			requested_command = cmd.params.split(None, 1)[0].lstrip("!").lower()
			if requested_command in self.command_methods:
				msg = self.command_methods[requested_command].__doc__
				self.send_privmsg(msg)
			else:
				self.send_privmsg(f"I don't know what '{requested_command}' is.")

	def send_privmsg(self, msg):
		sent_msg, num_sent_bytes = super().send_privmsg(msg)
		text_length = len(Privmsg.from_str(sent_msg).text)
		if text_length > TwitchBot.twitch_text_len_max:
			self.logger.warning(f"Message length {text_length} > {TwitchBot.twitch_text_len_max}")
		return sent_msg, num_sent_bytes

	def register_command(self, command_name, callback):
		copied_callback = functools.partial(callback)
		copied_callback.__doc__ = TwitchBot.format_usage_docstring(command_name, callback.__doc__)
		super().register_command(command_name.lower(), copied_callback)

	@staticmethod
	def get_user(prefix):
		return prefix.split("!", 1)[0]

	@staticmethod
	def format_usage_docstring(method_name, docstr):
		new_docstr = "Usage: "
		if docstr is None or docstr.strip() == "":
			new_docstr += "!" + method_name
		else:
			if docstr.split(None, 1)[0].lstrip("!") == method_name:
				new_docstr += "!" + docstr
			else:
				new_docstr += "!" + method_name + " " + docstr
		return new_docstr

	def _setup_commands(self):
		self._register_help_commands()

		command_functions = inspect.getmembers(
			self,
			lambda fn: hasattr(fn, "is_command_function") and fn.is_command_function
		)
		for name, method in command_functions:
			self.register_command(name.lower(), method)

	def _register_help_commands(self):
		help_fn = functools.partial(TwitchBot.send_supported_commands, self)
		help_fn.__doc__ = "Shows the usage for a command."
		for name in TwitchBot.help_command_names:
			self.register_command(name, help_fn)


