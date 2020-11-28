"""
Chapitre 11.4

Classes pour représenter un personnage utilisant des armes physiques.
"""


import random

import utils
from character import *


class Weapon(OffensiveMove):
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		super().__init__(name)
		self.power = power
		self.min_level = min_level

	def can_be_used_by(self, character):
		"""
		:param character: Le personnage avec lequel on vérifie la compatibilité.

		:returns: Vrai si le personnage peut utiliser l'arme, faux sinon.
		"""

		return character.level >= self.min_level

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)


class WeaponUser(Character):
	"""
	Un personnage qui utilise des armes physiques.

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param physical_attack: Le niveau d'attaque du personnage
	:param physical_defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.weapon = None
		self.last_move_used = None
	
	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, val):
		if val is None:
			val = Weapon.make_unarmed()
		if not val.can_be_used_by(self):
			raise ValueError(Weapon)
		self.__weapon = val

	def compute_damage(self, other):
		self.last_move_used = self.weapon
		return compute_damage_output(
			self.level,
			self.weapon.power,
			self.attack,
			other.defense,
			1/16,
			(0.85, 1.00)
		)


