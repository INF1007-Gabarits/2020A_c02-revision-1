"""
Exemple des notions du chapitre 7.
"""


from chatbot import *
from twitch_bot import *


def build_say_hi_callback(bot, message):
	def callback(*args):
		bot.send_privmsg(message)
	return callback

def run_ch7_example():
	bot = TwitchBot("logs")
	bot.register_command("say_hi", build_say_hi_callback(bot, "Haha! 'Tis I, the chatbot!"))
	bot.connect_and_join("oauth:...", "...", "chosson")
	bot.run()

