import sys
import random
from classes import person, enemy

character_classes: list[str, int, int, int] = [("Knight", 15, 8, 10), 
                                               ("Wizard", 8, 15, 10), 
                                               ("Ranger", 10, 8, 15)]

def create_hero(input_name: str, input_class: int):
    chosen_class = character_classes[input_class - 1]
    return person(name=input_name, character_class=chosen_class[0], strength=chosen_class[1], intelligence=chosen_class[2], dexterity=chosen_class[3])

def create_enemy(monsters: list[tuple[str, int, int, int]]) -> enemy:
    random_monster = random.choice(monsters)
    new_enemy = enemy(name = random_monster[0], base_health = random_monster[1], base_attack_damage = random_monster[2], base_experience_bounty = random_monster[3])
    return new_enemy

# def take_item(item_user: person, item: inventoryItem):
#     item_user.inventory.append(item)

# def use_item(item_user: person, item: inventoryItem) -> None:
#     item_user.health += item.health_boost
#     item_user.attack_damage += item.attack_boost

# def select_item(item_user: person, item: inventoryItem):
#     pass
def check_hit(attacker: person | enemy, defender: person | enemy) -> bool:
    # May need more balancing. if acc ~ eva, almost 100% to hit
    attack_accuracy: float = attacker.accuracy / defender.evasion
    return attack_accuracy > random.random()

def player_hit(damage: int, player: person, enemy: enemy) -> None:
    if check_hit(player, enemy):
        print(f"You hit {enemy.name} and dealt {damage} damage! \nENEMY HP: {enemy.health}/{enemy.max_health}\n")
        enemy.take_damage(damage)
    else:
        print("Your attack missed. Aim better")

def enemy_hit(player: person, enemy: enemy) -> None:
    if check_hit(enemy, player):
        enemy_damage: int = enemy.attack()
        print(f"{enemy.name} hit you and dealt {enemy_damage} damage! \nPLAYER HP: {player.health}/{player.max_health}\n")
        player.take_damage(enemy_damage)
    else:
        print(f"You dodged {enemy.name}'s attack.")

# TODO: Need to exit fight monster is killed before they can attack
def battle(player: person, enemy: enemy):
    print("===== BATTLE START =====\n")
    print(f"A {enemy.name} has appeared!\n")
    enemy.display_info()
    while player.health >= 0 and enemy.health >= 0:
        print(f"PLAYER HP: {player.health}/{player.max_health} // {enemy.name} HP: {enemy.health}/{enemy.max_health}\n")
        action_choice = input("Choose your action:\n(A) Attack\n(K) Kick\n(P) Use Potion\n(I) View Player Info\n(E) Exit\n\nInput: ").lower()
        print()
        match action_choice:
            case "a":
                player_damage = player.attack()
                player_hit(damage=player_damage, player=player, enemy=enemy)
                enemy_hit(player=player, enemy=enemy)
            case "k":
                if player.level >= 3:
                    player_damage = player.kick()
                    player_hit(damage=player_damage, player=player, enemy=enemy)
                    enemy_hit(player=player, enemy=enemy)
                else:
                    print("Careful! You aren't strong enough for that yet.")
            case "p":
                # TODO: Add check for what kind of potion to use and don't prompt enemy attack unless potion is actually used
                player.use_potion()
                enemy_hit(player=player, enemy=enemy)
            case "i":
                player.display_info()
            case "e":
                sys.exit()
        print("   ///////////////////////////////////////////////////////////////\n")

    if enemy.health <= 0:
        print(f"You've slain the enemy {enemy.name}! You gained {enemy.experience_bounty} experience!\n")
        player.experience += enemy.experience_bounty
        if player.experience >= player.experience_cap:
            player.level_up()

