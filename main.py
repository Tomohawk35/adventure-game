# import random
import sys
# from dataclasses import dataclass
from classes import person, enemy, inventoryItem
from functions import create_hero, create_enemy, fight, battle

# name / base_health / base_attack_damage / base_experience_bounty
monster_types: list[str, int]= [("Goblin", 30, 5, 10), 
                                ("Harpy", 25, 8, 10), 
                                ("Orc", 45, 10, 15),
                                ("Dragon", 80, 30, 80),
                                ("Frog", 10, 2, 2),
                                ("Zombie", 30, 10, 15)]

character_classes: list[str] = ["Knight", "Wizard", "Ranger"]

def main():
    input_name: str = input("\nWhat is your name? ").title()
    input_class: str = input(f"What is your job: {character_classes[0]}, {character_classes[1]}, or {character_classes[2]}? ").strip().lower()
    player1: person = create_hero(input_name, input_class)
    print("\n===== A NEW HERO HAS ARRIVED! ===== \n")
    print(f"Welcome to Evendale, {player1.name} the {player1.character_class}.\n")

    while True: 
        user_input = input("What would you like to do:\n(F) Fight\n(E) Exit\n\nInput: ").lower()
        print()
        match user_input:
            case "e": 
                sys.exit()
            case "f":
                new_enemy = create_enemy(monster_types)
                battle(player1, new_enemy)

if __name__ == "__main__":
    main()