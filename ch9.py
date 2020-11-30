"""
Exemple des notions du chapitre 9.
"""


import argparse
import sys
from collections import namedtuple

from chatbot import *
from twitch_bot import *
from ch8 import *

def parse_args():
	arg_parser = argparse.ArgumentParser(
		description="Run custom chatbot.",
		epilog="Made by me."
	)
	arg_parser.add_argument(
		# TODO: Ajouter l'option --config-file
		# TODO: mettre la destination à config_file
		# TODO: Chosir le bon type de nargs (https://docs.python.org/3/library/argparse.html#nargs)
		action="store", nargs=...,
		# TODO: L'argument doit être obligatoire.
		type=str, metavar="INI_FILE",
		help="The INI file containing login and target chat information."
	)
	arg_parser.add_argument(
		# TODO: Ajouter l'option --quotes-file
		# TODO: mettre la destination à quotes_file
		# TODO: Chosir le bon type de nargs
		action="store", nargs=...,
		# TODO: L'argument doit être obligatoire.
		type=str, metavar="JSON_FILE",
		help="The JSON file containing the various quotes supported by the !quote command."
	)
	return arg_parser.parse_args(sys.argv[1:])

def run_ch9_example():
	opts = parse_args()
	# TODO: Passer les noms de fichiers à la fonction du chapitre 8.

