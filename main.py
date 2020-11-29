"""
Main function, runs the bot.
"""


import sys
import os
import argparse
import configparser
import json
import random
from collections import namedtuple

from chatbot import *
from twitch_bot import *
from my_bot import MyBot


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

def build_say_hi_callback(bot, message):
	def callback(*args):
		bot.send_privmsg(message)
	return callback

def run_ch7_example():
	bot = TwitchBot("logs")
	bot.register_command("say_hi", build_say_hi_callback(bot, "Haha! 'Tis I, the chatbot!"))
	bot.connect_and_join("oauth:...", "...", "chosson")
	bot.run()

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

def parse_args():
	arg_parser = argparse.ArgumentParser(
		description="Run custom chatbot.",
		epilog="Made by me."
	)
	arg_parser.add_argument(
		"--config-file",
		dest="config_file",
		action="store", nargs="?",
		required=True,
		type=str, metavar="INI_FILE",
		help="The INI file containig login and target chat information."
	)
	arg_parser.add_argument(
		"--quotes-file",
		dest="quotes_file",
		action="store", nargs="?",
		required=True,
		type=str, metavar="JSON_FILE",
		help="The JSON file containing the various quotes supported by the !quote command."
	)
	return arg_parser.parse_args(sys.argv[1:])

def run_ch9_example():
	opts = parse_args()
	run_ch8_example(opts.config_file, opts.quotes_file)


def main():
	chapter_example = "ch7"

	if chapter_example == "ch7":
		run_ch7_example()
		return
	elif chapter_example == "ch8":
		run_ch8_example("data/config.ini", "data/quotes.json")
		return
	elif chapter_example == "ch9":
		run_ch9_example()
		return
	elif chapter_example == "ch11":
		opts = parse_args()

		config = load_config(opts.config_file)
		quotes = load_quotes(opts.quotes_file)

		bot = MyBot("logs", quotes)
		bot.connect_and_join(config.password, config.nickname, config.channel)
		bot.run()

if __name__ == "__main__":
	main()
