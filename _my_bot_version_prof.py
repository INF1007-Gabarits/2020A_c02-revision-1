"""
Un chatbot qui s'identifie et donnes des citations aléatoires.
"""

import random

from chatbot import *
from twitch_bot import *


class MyBot(TwitchBot):
	def __init__(self, logs_folder, quotes):
		# Construire la classe parent en lui passant le dossier de journaux.
		super().__init__(logs_folder)
		# On garde le dictionnaire de citations (paramètre `quotes`) dans une variable d'instance.
		self.quotes = quotes

	# TODO: Ajouter une commande "say_hi" (à l'aide du décorateur TwitchBot.command) qui répond avec un message de la forme:
	#       "My name is <nom-du-bot>. You killed my father. Prepare to die.", où <nom-du-bot> est le nom du compte utilisé par le chatbot.
	#       Indice : Dans la méthode connect_and_join de TwitchBot, le nom (nickname) du bot est gardé comme attribut.
	@TwitchBot.new_command
	def say_hi(self, cmd: Chatbot.Command):
		self.send_privmsg(f"My name is {self.nickname}. You killed my father. Prepare to die.")

	# TODO: Ajouter une commande "quote" qui répond de trois façons selon ce qui suit le nom de la commande dans le message.
	@TwitchBot.new_command
	def quote(self, cmd: Chatbot.Command):
		# Si un nom de catégorie est donné (on trouve les paramètres de la commande dans cmd.params) :
		if cmd.params is not None:
			# Si la catégorie est connue, on envoie au hasard une citation venant de cette catégorie si elle est connue, sinon
			if cmd.params in self.quotes:
				self.send_privmsg(random.choice(self.quotes[cmd.params]))
			# Sinon, on envoie un message disant que la catégorie est inconnue (ex. "Unrecognized category 'la_catégorie'")
			else:
				self.send_privmsg(f"Unrecognized category '{cmd.params}'.")
		# Si aucune catégorie n'est fournie, on choisit au hasard une catégorie puis une citation (comme dans l'exemple du chapitre 8)
		else:
			random_category = random.choice(tuple(self.quotes.keys()))
			random_quote = random.choice(self.quotes[random_category])
			self.send_privmsg(random_quote)
