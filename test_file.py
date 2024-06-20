from dataclasses import dataclass
import random

@dataclass
class enemy:
    name: str
    level: int = 1
    base_health: int = 50
    max_health: int = base_health + (20 * (level - 1))
    health: int = max_health
    base_attack_damage: int = 10
    attack_damage: int = base_attack_damage + (5 * (level - 1))
    base_experience_bounty: int = 50
    experience_bounty: int = base_experience_bounty * level

    def attack(self) -> int:
        return self.attack_damage + random.randint(-10, 10)
    
    def take_damage(self, damage) -> None:
        self.health -= damage

    def display_info(self) -> None:
        print(f"===== {self.name.upper()} INFO =====\nHP: {self.health}/{self.max_health} // LEVEL: {self.level}\n")

# name / base_health / base_attack_damage / base_experience_bounty
monster_types = [("Goblin", 30, 5, 10), ("Harpy", 25, 8, 10), ("Orc", 45, 10, 15)]
length = len(monster_types)
r = random.choice(monster_types)
print(r)

def create_enemy(monsters) -> enemy:
    random_monster = random.choice(monsters)
    return enemy(name = random_monster[0], base_health = random_monster[1], base_attack_damage = random_monster[2], base_experience_bounty = random_monster[3])
enemy_monster = create_enemy()