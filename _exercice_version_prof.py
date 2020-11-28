"""
Chapitre 11.4
"""


import math
from inspect import *
from abc import *

from game import *
from weapon_user import *
from spellcaster import *
from magician import *
from warrior import *


def simulate_battle():
	c1 = WeaponUser(
		name="Äpik",
		level=70,
		max_hp=500,
		attack=150,
		defense=70,
	)
	c2 = Warrior(
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
	c2.weapon = HeavyWeapon("Nerf Battle Axe", 120, 60)
	c2.strong_blows = True
	c3.spell = Spell("Big Chungus Power", 100, 35, 50)
	c3.weapon = Weapon("Slingshot", 80, 20)
	c3.using_magic = True
	c4.spell = Spell("Big Fire", 120, 40, 50)

	turns = run_battle(c3, c2)
	print(f"The battle ended in {turns} turns.")


class A(ABC):
	def __init__(self, p1, p2, **kwargs):
		self.__p1 = p1
		self.__p2 = p2
		print("A.__init__()")
	
	@property
	def p1(self):
		return self.__p1
	
	@property
	def p2(self):
		return self.__p2

class B(A):
	def __init__(self, p3, **kwargs):
		super().__init__(**kwargs)
		self.__p3 = p3
		print("B.__init__()")
	
	@property
	def p3(self):
		return self.__p3

class C(A):
	def __init__(self, p4, **kwargs):
		super().__init__(**kwargs)
		self.__p4 = p4
		print("C.__init__()")
	
	@property
	def p4(self):
		return self.__p4

class D(B, C):
	# MRO: D -> B -> C -> A
	def __init__(self, p1, p2, p3, p4):
		super().__init__(p1=p1, p2=p2, p3=p3, p4=p4)
		print("D.__init__()")


def main():
	simulate_battle()

	#c = C(p1=1, p2=2, p4=4)
	#print(c.p1, c.p2, c.p4)
	#b = B(1, 2, 3)
	#print(b.p1, b.p2, b.p3)
	#d = D(p1=1, p2=2, p3=3, p4=4)
	#print(D.mro())

if __name__ == "__main__":
	main()

