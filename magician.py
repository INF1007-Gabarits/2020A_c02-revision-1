"""
Chapitre 11.4

Classes pour représenter un magicien et ses pouvoirs magiques.
"""


import random

import utils
from character import *
from spellcaster import *
from weapon_user import *


class Magician(WeaponUser, Spellcaster):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	# TODO: Surcharger la méthode `compute_damage` 
		# Si on veut et peut utiliser de la magie (`will_use_spell()`):
			# TODO: Utiliser le `compute_damage` de `Spellcaster`
		# Sinon
			# TODO: Utiliser le `compute_damage` de `WeaponUser`

	def will_use_spell(self):
		return self.using_magic and self.can_use_spell()
