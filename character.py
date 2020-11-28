"""
Chapitre 11.4

Classes pour représenter un personnage.
"""


import random
from abc import *

import utils


def compute_damage_output(level, power, attack, defense, crit_chance, random_range):
	level_factor = (2 * level) / 5 + 2
	weapon_factor = power
	atk_def_factor = attack / defense
	critical = random.random() <= crit_chance
	modifier = (2 if critical else 1) * random.uniform(*random_range)
	damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier
	return int(round(damage)), critical


class OffensiveMove(ABC):
	def __init__(self, name):
		self.__name = name

	@property
	def name(self):
		return self.__name

	@abstractmethod
	def can_be_used_by(self, character):
		raise NotImplementedError()


class Character(ABC):
	def __init__(self, name, level, max_hp, attack, defense):
		self.__name = name
		self.level = level
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.hp = max_hp
	
	@property
	def name(self):
		return self.__name

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	@property
	def last_move_used(self) -> OffensiveMove:
		return self.__last_move_used

	@last_move_used.setter
	def last_move_used(self, val: OffensiveMove):
		self.__last_move_used = val

	@abstractmethod
	def compute_damage(self, other):
		raise NotImplementedError()

	def take_damage(self, dmg):
		self.hp -= dmg

