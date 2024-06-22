from dataclasses import dataclass
import random
from classes import person, equipment
from functions import create_hero

player = create_hero("tyler",1)
print(player.strength, player.intelligence, player.dexterity, sep=", ")
print(f"player attack is {player.attack_damage}")
sword = equipment("sword", "Weapon", attack_boost=5)
sword.equip(player)
print(f"player attack is {player.attack_damage}")
sword.unequip(player)
print(f"player attack is {player.attack_damage}")

