"""
Main function, runs the bot.
"""


import sys
import os
import argparse
import configparser
import json
from collections import namedtuple

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


def main():
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
	opts = arg_parser.parse_args(sys.argv[1:])

	config = load_config(opts.config_file)
	quotes = load_quotes(opts.quotes_file)

	bot = MyBot("logs", quotes)
	bot.connect_and_join(config.password, config.nickname, config.channel)
	bot.run()

if __name__ == "__main__":
	main()
