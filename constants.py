# name / base_health / base_attack_damage / base_experience_bounty
monster_types: list[tuple[str, int, int, int]] = [("Goblin", 30, 5, 10),
                                                  ("Harpy", 25, 8, 10),
                                                  ("Orc", 45, 10, 15),
                                                  ("Frog", 10, 2, 2),
                                                  ("Zombie", 30, 10, 15)]

boss_types: list[tuple[str, int, int, int]] = [("Dragon", 80, 30, 80),
                                               ("Mindflayer", 70, 20, 70)]

# name / strength / intelligence / dexterity
character_classes: list[tuple[str, int, int, int]] = [("Knight", 15, 8, 10), ("Wizard", 8, 15, 10), ("Ranger", 10, 8, 15)]

damage_types: list[str] = ["Fire", "Water", "Lightning", "Poison"]

equipment_types: list[str] = ["Helmet", "Body Armor", "Weapon", "Offhand", "Gloves", "Belt", "Ring", "Boots"]
