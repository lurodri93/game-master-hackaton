import random

TRAITS_TABLES = {
    "physique": ["Atlético", "Musculoso", "Corpulento", "Delicado", "Demacrado", "Grueso", "Larguirucho", "Fibrado",
                 "Tosco", "Flaco", "Bajito", "Nervudo", "Esbelto", "Flácido", "Atractivo", "Fuerte", "Pequeño",
                 "Imponente", "Flexible", "Nervioso"],
    "face": ["Franca", "Hinchada", "Cincelada", "Aguileña"],
    "skin": ["Cicatriz", "Quemada", "Oscura", "Pálida"],
    "hair": ["Calvo", "Trenzado", "Rizado", "Grasiento"],
    "clothing": ["Elegante", "Raído", "Ensangrentado", "Decorado"],
    "virtue": ["Valiente", "Justo", "Leal", "Piadoso"],
    "vice": ["Agresivo", "Cruel", "Mentiroso", "Perezoso"],
    "speech": ["Grave", "Murmurosa", "Formal", "Tartamudeo"],
    "background": ["Ladrón", "Clérigo", "Mercenario", "Contrabandista"],
    "misfortune": ["Maldito", "Cazado", "Robado", "Exiliado"],
    "alignment": ["Leal", "Neutral", "Caótico"]
}

DUNGEON_GEAR = ["Cuerda 50ft", "Velas", "Martillo", "Antorchas"]
GEAR1 = ["Pala", "Fuelle", "Grasa", "Cubo"]
GEAR2 = ["Incienso", "Perfume", "Botella", "Jabón"]

def pick_random_from_table(table):
    if table == "dungeon":
        return random.choice(DUNGEON_GEAR)
    elif table == "gear1":
        return random.choice(GEAR1)
    elif table == "gear2":
        return random.choice(GEAR2)
    elif table in TRAITS_TABLES:
        return random.choice(TRAITS_TABLES[table])
    return "¿?"

