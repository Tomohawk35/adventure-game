# import random
import sys
# from dataclasses import dataclass
from classes import person, enemy
from functions import create_hero, create_enemy, battle
import constants

def main():
    input_name: str = input("\nWhat is your name? ").title()
    input_class: int = int(input(f"What is your job: (1) {constants.character_classes[0][0]}, (2) {constants.character_classes[1][0]}, or (3) {constants.character_classes[2][0]}? ").strip())
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
                new_enemy = create_enemy(constants.monster_types)
                battle(player1, new_enemy)

if __name__ == "__main__":
    main()