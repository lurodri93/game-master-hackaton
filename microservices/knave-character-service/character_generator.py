import random
from utils import pick_random_from_table, TRAITS_TABLES

def generate_character(name: str):
    stats = {}
    flat_stats = {}
    for stat in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
        dice = sorted([random.randint(1, 6) for _ in range(3)])
        bonus = dice[0]
        defense = bonus + 10
        stats[stat] = {"bonus": bonus, "defense": defense}
        flat_stats[f"{stat}_bonus"] = bonus
        flat_stats[f"{stat}_defense"] = defense

    hp = random.randint(1, 8)

    weapon = random.choice(["Daga", "Espada", "Maza", "Hacha", "Bastón", "Honda", "Arco", "Ballesta"])

    armor_roll = random.randint(1, 20)
    if armor_roll <= 3:
        armor = "Sin armadura"
    elif armor_roll <= 14:
        armor = "Cuero (Def 12)"
    elif armor_roll <= 19:
        armor = "Acolchada (Def 13)"
    else:
        armor = "Cota de malla (Def 14)"

    shield_roll = random.randint(1, 20)
    if shield_roll <= 13:
        shield = "Ninguno"
    elif shield_roll <= 16:
        shield = "Casco (+1)"
    elif shield_roll <= 19:
        shield = "Escudo (+1)"
    else:
        shield = "Casco y Escudo (+2)"

    inventory = {
        "inventory_weapon": weapon,
        "inventory_armor": armor,
        "inventory_shield": shield,
        "dungeon_gear": pick_random_from_table("dungeon"),
        "gear1": pick_random_from_table("gear1"),
        "gear2": pick_random_from_table("gear2")
    }

    traits = {f"traits_{k}": pick_random_from_table(k) for k in TRAITS_TABLES}

    full_data = {
        "name": name,
        "level": 1,
        "experience": 0/500,
        "hit_points": hp,
        **flat_stats,
        **inventory,
        **traits,
    }

    full_data["raw_json"] = str(full_data)
    return full_data