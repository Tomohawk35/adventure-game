# import random
import sys
# from dataclasses import dataclass
from classes import person, enemy, inventoryItem
from functions import create_enemy, fight, battle

# name / base_health / base_attack_damage / base_experience_bounty
monster_types = [("Goblin", 30, 5, 10), 
                 ("Harpy", 25, 8, 10), 
                 ("Orc", 45, 10, 15)]
 
def main():
    print()
    input_name = input("What is your name? ")
    player1 = person(input_name)
    print("\n===== A NEW HERO HAS ARRIVED! ===== \n")
    print(f"Welcome to Evendale, {player1.name}.\n")
    # conversation = 0

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