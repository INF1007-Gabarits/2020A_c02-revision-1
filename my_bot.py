"""
A specific bot linked with the widget server.
"""

import sys
import time
import os
import random
import argparse
import subprocess

import requests

from irc import *
from chatbot import *
from twitch_bot import *


class MyBot(TwitchBot):
	def __init__(self, logs_folder, quotes):
		super().__init__(logs_folder, log_to_console=True, pokemon_exception_handling=True)
		self.quotes = quotes

	@TwitchBot.command
	def say_hi(self, cmd: Chatbot.Command):
		self.send_privmsg(f"Haha! 'Tis I, {self.nickname}!")

	@TwitchBot.command
	def quote(self, cmd: Chatbot.Command):
		if cmd.params is not None:
			if cmd.params in self.quotes:
				self.send_privmsg(random.choice(self.quotes[cmd.params]))
			else:
				self.send_privmsg(f"Unrecognized category '{cmd.params}'.")
		else:
			random_category = random.choice(tuple(self.quotes.keys()))
			random_quote = random.choice(self.quotes[random_category])
			self.send_privmsg(random_quote)
