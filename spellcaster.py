"""
Chapitre 11.4

Classes pour représenter un personnage avec des pouvoirs magiques.
"""


import random

import utils
from character import *
from weapon_user import Weapon


class Spell(Weapon):
	"""
	Un sort dans le jeu.

	:param name: Le nom du sort
	:param power: Le niveau d'attaque
	:param mp_cost: Le coût en MP d'utilisation du sort
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	def __init__(self, name, power, mp_cost, min_level):
		super().__init__(name, power, min_level)
		self.mp_cost = mp_cost


class Spellcaster(Character):
	"""
	Un utilisateur de magie dans le jeu.

	:param max_mp: MP maximum
	:param magic_attack: Le niveau d'attaque magique du personnage
	:param kwargs: Les autres paramètres à passer au parent
	"""

	def __init__(self, max_mp, magic_attack, **kwargs):
		super().__init__(**kwargs)
		self.max_mp = max_mp
		self.magic_attack = magic_attack
		self.mp = max_mp
		self.spell = None

	@property
	def mp(self):
		return self.__mp

	@mp.setter
	def mp(self, val):
		self.__mp = utils.clamp(val, 0, self.max_mp)

	@property
	def spell(self):
		return self.__spell

	@spell.setter
	def spell(self, val):
		if val is not None and not val.can_be_used_by(self):
			raise ValueError()
		self.__spell = val

	def compute_damage(self, other):
		if self.can_use_spell():
			self.mp -= self.spell.mp_cost
			self.last_move_used = self.spell
			return self._compute_magical_damage(other)
		else:
			self.last_move_used = None
			return (0, False)

	def can_use_spell(self):
		return self.spell is not None and self.mp >= self.spell.mp_cost

	def _compute_magical_damage(self, other):
		return compute_damage_output(
			self.level + self.magic_attack,
			self.spell.power,
			1,
			1,
			1/8,
			(0.85, 1.00)
		)

