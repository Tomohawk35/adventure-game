# import random
import sys
# from dataclasses import dataclass
from classes import person, enemy, inventoryItem
from functions import battle

global conversation
conversation = 0



    
#         elif user_input.lower() == "s":
#             return "You have an adrenaline injection (a) and some bandages (b) on you. Choose which one you will use, if any."
#         elif user_input.lower() in ["a", "b"]:
#             return use_item(user_input.lower(), son)
#         else:
#             return "father looks at you, waiting for your next move."


# def generate_dad_joke():
#     """
#     Generate a randome dad joke.
#     """
#     dad_jokes = ["Why couldn't the bicycle stand up by itself? Because it was two-tired!", 
#                  "I'm reading a book on anti-gravity. It's impossible to put down!",
#                  "Did you hear about the cheese factory that exploded? There was nothing left but de-brie!", 
#                  "Why don't scientists trust atoms? Because they make up everything!",
#                  "I used to play piano by ear, but now I use my hands.", 
#                  "Why did the scarecrow win an award? Because he was outstanding in his field!",
#                  "What do you call fake spaghetti? An impasta!",
#                  "Why don't skeletons fight each other? They don't have the guts!",
#                  "What did the janitor say when jumped out of the closet? Supplies!",
#                  "How do you organize a space party? You planet!",
#                  "I'm reading a book on the history of glue. I just can't seem to put it down!",
#                  "What do you call a fake noodle? An impasta!", 
#                  "Why did the coffee file a police report? It got mugged!",
#                  "Why was the math book sad? Because it had too many problems!",
#                  "Why does the sun smell bad? It's always gassy!",
#                  "Why did the knife graduate at the top of its grade? It's really sharp!"]
#     return random.choice(dad_jokes)

# def handle_input(user_input: person, son: person, father: person):

#     global conversation 

#     match conversation:
#         case 0:
#             match user_input:
#                 case "hey dad":
#                     return generate_dad_joke()
                
#                 case "i'm hungry.":
#                     return "Hey hungry, I'm dad!"
                
#                 case "bye dad.":
#                     return "Wait, just one more, okay?"
                
#                 case "fight me!":
#                     conversation = 1
#                     return f"Father: HP = {father.health}, DMG = {father.attack_damage}. Enter F to fight or S to view items in your inventory."
                
#                 case _:
#                     return "Huh? I didn't hear ya there, son. Anyways, want to hear some jokes of mine?"
                
#         case 1: 
#             if user_input == "f":
#                 son_damage = son.attack()
#                 father.take_damage(son_damage)
#                 response = f"You shanked your father and dealt {son_damage} damage! DAD'S HP = {father.health}\n"

#                 if father.health <= 0:
#                     conversation = 2
#                     son.health += 30
#                     son.attack_damage += 10
#                     return response + "You killed your father, you monster!\n" + "You have leveled up! Damage increased. Health increased. New ability unlocked: Kick (K to use)."


#     elif conversation == 1: 
#         if user_input.lower() == "f": 
#             son_damage = son.attack_enemy() 
#             father.take_damage(son_damage) 
#             response = f"You shanked your father and dealt {son_damage} damage! FATHER HP = {father.health}\n"

#             if father.health <= 0:
#                 conversation = 2
#                 son.health = 80
#                 son.attack = 30
#                 return response + "You killed your father, you monster! leveled up to level 2, damage increased, hp increased. new ability unlocked, kick (K to use).. (enter 'c' to continue, or 'cya' to leave.)"
                  
#             father_damage = father.attack_son()
#             son.take_damage(father_damage)
#             response += f"Your father hit you with his belt and dealt {father_damage} damage! SON HP = {son.health}"
        
#             if son.health <= 0:
#                 conversation = 4
#                 father.health = 100
#                 son.health = 50
#                 son.attack = 20
#                 return response + "\nYour father defeated you! but you know that this will not last for long, for you will get your revenge. WEAKLING END"
        
#             return response
    
#         elif user_input.lower() == "s":
#             return "You have an adrenaline injection (a) and some bandages (b) on you. Choose which one you will use, if any."
#         elif user_input.lower() in ["a", "b"]:
#             return use_item(user_input.lower(), son)
#         else:
#             return "father looks at you, waiting for your next move."
#     elif conversation == 2:
#         if user_input == "c":
#             conversation = 3
#             return "after you killed your father, you have been on the run from he police. today, one of them caught you. press F to fight, S to view items in storage."       
       
#     elif conversation == 3:
#         if user_input.lower() == "f":
#             son_damage = son.attack_enemy()
#             cop.take_damage(son_damage)
#             response = f"You shanked the cop and dealt {son_damage} damage! COP HP = {cop.health}\n"
        
#             if cop.health <= 0:
#                 print ("You became a feared criminal, wreaking havoc upon your home country. BAD END.")            
        
#             cop_damage = cop.attack_son()
#             son.take_damage(cop_damage)
#             response += f"the cop shot you and dealt {cop_damage} damage! SON HP={son.health}"
        
#             if son.health <= 0:
#                 conversation = 4
#                 cop.health = 120
#                 son.health = 50
#                 son.attack = 20
#                 return response + "\nThe cop imprisoned you! You swear to break out one day and get your revenge. PRISONER END"
    
#             return response
    
#         elif user_input.lower() == "s":
#             return "you have an adrenaline injection (a) and some bandages (b) on you. choose which one you will use, if any."
#         elif user_input.lower() in ["a", "b", "k"]:
#             return use_item(user_input.lower(), son)
#         else:
#             return "The cop glares at you."
        
# def use_item(user_input, son): 
#     """handle item usage""" 
#     global conversation 
#     if user_input == "a": 
#         son.health -= 20 
#         son.attack += 5 
#         if son.health <= 0: 
#             conversation = 4 
#             return "you overdosed on adrenaline! ADDICT END" 
#         return "you used the adrenaline injection and got a boost in damage but your HP decreased!" 
#     elif user_input == "b": 
#         son.health += 5 
#         son.attack -= 1 
#         return "you patched up a wound and got a health boost but your damage decreased!" 
#     elif user_input == "K": 
#         if conversation == 3: 
#             son.attack *= 2 
#             cop.attack *= 3 
#             return "you kicked the cop to enrage him, weakening his defense but multiplying his damage by 3!" 
#         else: return "you don't have the guts to kick your own father."

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
                new_enemy = enemy("Goblin")
                battle(player1, new_enemy)
        
        # print(handle_input(user_input, timmy, dad)) 
        # if conversation == 4: 
        #     break

if __name__ == "__main__":
    main()