"""
Un chatbot qui s'identifie et donnes des citations aléatoires.
"""

import random

from chatbot import *
from twitch_bot import *


class MyBot(TwitchBot):
	def __init__(self, logs_folder, quotes):
		# Construire la classe parent en lui passant le dossier de journaux.
		# On garde le dictionnaire de citations (paramètre `quotes`) dans une variable d'instance.
		pass

	# TODO: Ajouter une commande "say_hi" (à l'aide du décorateur TwitchBot.command) qui répond avec un message de la forme:
	#       "My name is <nom-du-bot>. You killed my father. Prepare to die.", où <nom-du-bot> est le nom du compte utilisé par le chatbot.
	#       Indice : Dans la méthode connect_and_join de TwitchBot, le nom (nickname) du bot est gardé comme attribut.

	# TODO: Ajouter une commande "quote" qui répond de trois façons selon ce qui suit le nom de la commande dans le message.
		# Si un nom de catégorie est donné (on trouve les paramètres de la commande dans cmd.params) :
			# Si la catégorie est connue, on envoie au hasard une citation venant de cette catégorie si elle est connue, sinon
			# Sinon, on envoie un message disant que la catégorie est inconnue (ex. "Unrecognized category 'la_catégorie'")
		# Si aucune catégorie n'est fournie, on choisit au hasard une catégorie puis une citation (comme dans l'exemple du chapitre 8)

