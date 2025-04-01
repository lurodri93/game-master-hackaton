# Documentación de Airtable

Este proyecto utiliza Airtable como base de datos para almacenar tanto personajes como enemigos, permitiendo la persistencia de las partidas y el acceso dinámico desde los agentes en N8N.

---

## 🔶 Base: `Hackaton`

### 📁 Tabla: `characterDB`

Esta tabla almacena toda la información relacionada con los personajes de los jugadores.

| Campo | Descripción |
|-------|-------------|
| `player_id` | Identificador único del jugador |
| `name` | Nombre del personaje |
| `level` | Nivel actual del personaje |
| `experience` | Puntos de experiencia acumulados |
| `hit_points` | Puntos de golpe actuales del personaje |
| `strength_bonus` | Bonificador de Fuerza |
| `strength_defense` | Defensa de Fuerza |
| `dexterity_bonus` | Bonificador de Destreza |
| `dexterity_defense` | Defensa de Destreza |
| `constitution_bonus` | Bonificador de Constitución |
| `constitution_defense` | Defensa de Constitución |
| `intelligence_bonus` | Bonificador de Inteligencia |
| `intelligence_defense` | Defensa de Inteligencia |
| `wisdom_bonus` | Bonificador de Sabiduría |
| `wisdom_defense` | Defensa de Sabiduría |
| `charisma_bonus` | Bonificador de Carisma |
| `charisma_defense` | Defensa de Carisma |
| `inventory_weapon` | Arma equipada |
| `inventory_armor` | Armadura equipada |
| `inventory_shield` | Escudo equipado |
| `dungeon_gear` | Equipo de mazmorra aleatorio |
| `gear1` | Equipo adicional 1 |
| `gear2` | Equipo adicional 2 |
| `traits_physique` | Rasgo físico del personaje |
| `traits_face` | Rasgo facial |
| `traits_skin` | Tipo de piel |
| `traits_hair` | Tipo de cabello |
| `traits_clothing` | Estilo de ropa |
| `traits_virtue` | Virtud |
| `traits_vice` | Vicio |
| `traits_speech` | Estilo de habla |
| `traits_background` | Trasfondo del personaje |
| `traits_misfortune` | Desgracia o problema |
| `traits_alignment` | Alineamiento moral |
| `raw_json` | Campo opcional que contiene el JSON original completo del personaje, útil para reconstrucción o debug |

---

### 📁 Tabla: `monsterDB`

Contiene todos los monstruos adaptados al sistema Knave, ya sea manualmente o extraídos del bestiario OSR y transformados con las reglas de adaptación (HP = HD x 4/5).

| Campo | Descripción |
|-------|-------------|
| `name` | Nombre del monstruo |
| `hd` | Dados de golpe originales |
| `hp` | Puntos de golpe adaptados (HD * 4 o 5) |
| `ac` | Defensa de armadura |
| `attacks` | Descripción de los ataques |
| `morale` | Moral del monstruo |
| `movement` | Movimiento |
| `save_as` | Nivel de salvación que representa su defensa en Knave |
| `number_appearing` | Número de enemigos que aparecen |
| `description` | Breve descripción del enemigo |
| `special` | Habilidades o poderes especiales |

---

## 📌 Notas de uso

- El agente Game Master puede leer y escribir directamente en estas tablas desde N8N mediante llamadas a la API de Airtable.
- El microservicio de generación de personajes envía la información completa en formato JSON para insertar directamente en `characterDB`.
- Para insertar enemigos, se recomienda tener una función que consulte aleatoriamente un enemigo y lo adapte si es necesario antes del combate.

---

## 🔐 Seguridad

- Usa claves de API personalizadas con permisos solo de lectura o escritura cuando sea necesario.
- Recomendamos separar las credenciales en un archivo `.env` y no subirlas al repositorio público.
