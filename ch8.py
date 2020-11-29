"""
Exemple des notions du chapitre 8.
"""


import configparser
import json
import random
from collections import namedtuple

from chatbot import *
from twitch_bot import *


ConfigInfo = namedtuple("ConfigInfo", ["nickname", "password", "channel"])

def load_config(filename):
	config = configparser.ConfigParser()
	config.read(filename)
	channel = config["chat"]["channel"]
	bot_nickname = config["login"]["account_name"]
	bot_password = config["login"]["account_oauth_token"]
	return ConfigInfo(bot_nickname, bot_password, channel)

def load_quotes(filename):
	return json.load(open(filename, "r", encoding="UTF-8"))

def build_quotes_callback(bot, quotes):
	def callback(*args):
		random_category = random.choice(tuple(quotes.keys()))
		random_quote = random.choice(quotes[random_category])
		bot.send_privmsg(random_quote)
	return callback

def run_ch8_example(config_filename, quotes_filename):
		config = load_config(config_filename)
		quotes = load_quotes(quotes_filename)
		bot = TwitchBot("logs")
		bot.register_command("quote", build_quotes_callback(bot, quotes))
		bot.connect_and_join(config.password, config.nickname, config.channel)
		bot.run()

