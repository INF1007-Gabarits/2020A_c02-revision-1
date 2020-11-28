"""
Chapitre 11.4
"""


import math
from inspect import *

from game import *
from weapon_user import *
from spellcaster import *
from magician import *


def simulate_battle():
	c1 = WeaponUser(
		name="Äpik",
		level=70,
		max_hp=500,
		attack=150,
		defense=70,
	)
	c2 = WeaponUser(
		name="Gämmör",
		level=80,
		max_hp=550,
		attack=100,
		defense=120,
	)
	c3 = Magician(
		name="Damn! That magic dude",
		level=75,
		max_hp=450,
		attack=80,
		defense=80,
		max_mp=100,
		magic_attack=150
	)
	c4 = Spellcaster(
		name="Fire Elemental",
		level=50,
		max_hp=300,
		attack=80,
		defense=80,
		max_mp=200,
		magic_attack=150
	)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)
	c3.spell = Spell("Big Chungus Power", 100, 35, 50)
	c3.weapon = Weapon("Slingshot", 80, 20)
	c3.using_magic = True
	c4.spell = Spell("Big Fire", 120, 40, 50)

	turns = run_battle(c4, c1)
	print(f"The battle ended in {turns} turns.")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

