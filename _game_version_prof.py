"""
Chapitre 11.4

Fonctions pour simuler un combat.
"""


import random

import utils
from character import *
from magician import *


def deal_damage(attacker, defender):
	damage, crit = attacker.compute_damage(defender)
	# TODO: Obtenir l'arme utilisée par l'attaquant.
	#       Si aucune arme n'a été utilisée (last_move_used est None), on affiche "nothing"
	weapon_used = attacker.last_move_used.name if attacker.last_move_used is not None else "nothing"
	defender.take_damage(damage)
	print(f"  {attacker.name} used {weapon_used}")
	if crit:
		print("    Critical hit!")
	print(f"    {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	attacker = c1
	defender = c2
	turns = 1
	print(f"{attacker.name} would like to battle.")
	print(f"{defender.name} accepted!")
	while True:
		deal_damage(attacker, defender)
		if defender.hp == 0:
			print(f"  {defender.name } is sleeping with the fishes.")
			break
		turns += 1
		attacker, defender = defender, attacker
	return turns
