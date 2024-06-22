from dataclasses import dataclass
import random, sys

@dataclass
class person:
    name: str
    character_class: str
    level: int = 1
    # Player Attributes
    strength: int = 10
    intelligence: int = 10
    dexterity: int = 10
    # Attribute-based stats
    base_max_health: int = 5 * strength
    base_max_mana: int = 5 * intelligence
    base_attack_damage: int = 20
    base_attack_speed: int = 20 # Need to work out formula for this and how it will be incorporated
    base_accuracy: int = 10 * dexterity
    base_evasion: int = 10 * dexterity
    base_crit_chance: float = 0.02 + (0.001 * dexterity)
    base_crit_multiplier: float = 1.5
    base_armour: int = 2
    experience_cap: int = 100 * level
    experience: int = 0
    # Attribute / Stat Modifiers
    modifier_max_health: int = 0
    modifier_max_mana: int = 0
    modifier_attack_damage: int = 0
    modifier_accuracy: int = 0
    modifier_evasion: int = 0
    modifier_flat_crit_chance: float = 0.0 # Decimal added flat crit chance
    modifier_increased_crit_chance: float = 0.0 # Decimal increased crit chance
    modifier_crit_multiplier: float = 0.0 # Decimal added crit multipler
    modifier_armour: int = 0
    # Stats
    max_health: int = base_max_health + modifier_max_health
    max_mana: int = base_max_mana + modifier_max_mana
    health: int = max_health
    mana: int = max_mana
    attack_damage: int = base_attack_damage + modifier_attack_damage
    accuracy: int = base_accuracy + modifier_accuracy
    evasion: int = base_evasion + modifier_evasion
    crit_chance: float = (base_crit_chance + modifier_flat_crit_chance) * (1 + modifier_increased_crit_chance)
    crit_multiplier: float = base_crit_multiplier + modifier_crit_multiplier
    armour = base_armour + modifier_armour
    # Items
    potion_count: int = 3 # TODO: Move to inventory? How to track quantities in inventory
    inventory = []
    # attack_choices: list[str, str] = [("A": "Attack"), ("P": "Use Potion")]

    def update_stats(self) -> None:
        self.max_health = self.base_max_health + self.modifier_max_health
        self.max_mana = self.base_max_mana + self.modifier_max_mana
        self.health = self.max_health
        self.mana = self.max_mana
        self.attack_damage = self.base_attack_damage + self.modifier_attack_damage
        self.accuracy = self.base_accuracy + self.modifier_accuracy
        self.evasion = self.base_evasion + self.modifier_evasion
        self.crit_chance = (self.base_crit_chance + self.modifier_flat_crit_chance) * (1 + self.modifier_increased_crit_chance)
        self.crit_multiplier = self.base_crit_multiplier + self.modifier_crit_multiplier
        self.armour = self.base_armour + self.modifier_armour

    def attack(self) -> int:
        return self.attack_damage + random.randint(-10, 10)
    
    def take_damage(self, damage) -> None:
        self.health -= damage
        if self.health <= 0:
            print("You fought valiantly but were defeated! \n\n ====== GAME OVER ======")
            sys.exit()
    
    def kick(self) -> int:
        if self.level >= 3:
            return self.attack_damage + random.randint(-5, 5) + 5
        else:
            print("Careful! You aren't strong enough for that yet.")
        
    def use_potion(self) -> None:
        if self.potion_count >= 1:
            self.potion_count -= 1
            self.health += 20 # TODO: make it so you can't go above max health
            print(f"You used a potion. You have {self.potion_count} potions left.")
            print(f"You are now at {self.health} health points.")
        else:
            print("You are out of potions.")

    def display_info(self) -> None:
        print(f"===== PLAYER INFO =====\nHP: {self.health}/{self.max_health} // LEVEL: {self.level} // POTIONS AVAILABLE: {self.potion_count} // PLAYER EXP: {self.experience}\n")

    def level_up(self) -> None:
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack_damage += 5
        self.experience = 0
        self.experience_cap = 100 * self.level
        print(f"{self.name} has leveled up! Damage and Health have been increased.\n")
        if self.level == 3:
            print("New ability unlocked: Kick (K to use)")




@dataclass
class enemy:
    name: str
    level: int = 1
    base_health: int = 50
    max_health: int = base_health + (20 * (level - 1))
    health: int = max_health
    base_attack_damage: int = 10
    base_accuracy: int = 100
    base_evasion: int = 100
    base_armour: int = 2
    attack_damage: int = base_attack_damage + (5 * (level - 1))
    accuracy: int = base_accuracy
    evasion: int = base_evasion
    armour: int = base_armour
    base_experience_bounty: int = 50
    experience_bounty: int = base_experience_bounty * level

    def attack(self) -> int:
        return self.attack_damage + random.randint(-10, 10)
    
    def take_damage(self, damage) -> None:
        self.health -= damage

    def display_info(self) -> None:
        print(f"===== {self.name.upper()} INFO =====\nHP: {self.health}/{self.max_health} // LEVEL: {self.level}\n")




@dataclass
class equipment:
    name: str
    equipment_type: str
    equipped_status: bool = False
    health_boost: int = 0
    mana_boost: int = 0
    attack_boost: int = 0
    accuracy_boost: int = 0
    evasion_boost: int = 0
    flat_crit_chance_boost: float = 0.0 # Decimal added flat crit chance
    increased_crit_chance_boost: float = 0.0 # Decimal increased crit chance
    crit_multiplier_boost: float = 0.0 # Decimal added crit multipler
    armour_boost: int = 0

    def equip(self, user: person) -> None:
        if self.equipped_status:
            print(f"{self.name} is already equipped.")
        else:
            print(f"{self.name} equipped.")
            self.equipped_status = True
            user.health += self.health_boost
            user.attack_damage += self.attack_boost
            user.modifier_max_health += self.health_boost
            user.modifier_max_mana += self.mana_boost
            user.modifier_attack_damage += self.attack_boost
            user.modifier_accuracy += self.accuracy_boost
            user.modifier_evasion += self.evasion_boost
            user.modifier_flat_crit_chance += self.flat_crit_chance_boost
            user.modifier_increased_crit_chance += self.increased_crit_chance_boost
            user.modifier_crit_multiplier += self.crit_multiplier_boost
            user.modifier_armour += self.armour_boost
            user.update_stats()

    def unequip(self, user: person) -> None:
        if self.equipped_status == False:
            print(f"{self.name} is already unequipped.")
        else:
            print(f"{self.name} unequipped.")
            self.equipped_status = False
            user.health -= self.health_boost
            user.attack_damage -= self.attack_boost
            user.modifier_max_health -= self.health_boost
            user.modifier_max_mana -= self.mana_boost
            user.modifier_attack_damage -= self.attack_boost
            user.modifier_accuracy -= self.accuracy_boost
            user.modifier_evasion -= self.evasion_boost
            user.modifier_flat_crit_chance -= self.flat_crit_chance_boost
            user.modifier_increased_crit_chance -= self.increased_crit_chance_boost
            user.modifier_crit_multiplier -= self.crit_multiplier_boost
            user.modifier_armour -= self.armour_boost
            user.update_stats()




@dataclass
class potion:
    name: str
    health_boost: int
    mana_boost: int

    def use(self, user: person):
        user.health += self.health_boost
        user.mana += self.mana_boost
        if user.health > user.max_health:
            user.health = user.max_health
        if user.mana > user.max_mana:
            user.mana = user.max_mana




@dataclass
class skill:
    name: str
    impact_damage: int = 10
    damage_type: str = "Fire" # Fire, Water, Lightning
    # TODO: How to incorporate damage over time? Just lower damage and a duration?