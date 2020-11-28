"""
Chapitre 11.4

Classes pour représenter un guerrier et des armes lourdes.
"""


import random

import utils
from character import *
from weapon_user import *


class HeavyWeapon(Weapon):
	def can_be_used_by(self, character):
		return isinstance(character, Warrior) and super().can_be_used_by(character)


class Warrior(WeaponUser):
	"""
	Classe représentant un guerrier (personnage spécialisé en armes). Un guerrier est la seule classe qui peut utiliser des armes lourdes.

	Un guerrier peut utiliser des armes lourdes et adopter soit un position défensive ou donner des coups particulièrement puissant. Lorsqu'il est en position défensive, les dégâts qu'il reçoit sont 25% moins forts, mais les coups qu'il porte sont aussi 25% moins puissants. En donnant des coups puissants, il y met toute sa force et fait 25% plus de dégâts, mais il a aussi 20% de chance de manquer ses coups. Les deux positions sont mutellement exclusives.
	"""

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.__strong_blows = False
		self.__defensive_stance = False

	@property
	def strong_blows(self):
		return self.__strong_blows

	@strong_blows.setter
	def strong_blows(self, val):
		if val:
			self.defensive_stance = False
		self.__strong_blows = val

	@property
	def defensive_stance(self):
		return self.__defensive_stance

	@defensive_stance.setter
	def defensive_stance(self, val):
		if val:
			self.strong_blows = False
		self.__defensive_stance = val

	def compute_damage(self, other):
		damage, crit = WeaponUser.compute_damage(self, other)
		if self.strong_blows:
			missed = random.random() <= 0.20
			return (damage * 1.25, crit) if not missed else (0, False)
		elif self.defensive_stance:
			return damage * 0.75, crit
		else:
			return damage, crit

	def take_damage(self, dmg):
		self.hp -= dmg * 0.75 if self.defensive_stance else dmg
