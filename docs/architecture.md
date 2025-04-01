# Arquitectura del Proyecto: Hackaton Game Master

## Componentes

### 🧠 1. Agente Principal: Game Master ("Señor oscuro")
- Implementado con GPT-4 (OpenAI) como modelo base.
- Ejecutado mediante el nodo `langchain.agent` en N8N.
- Interactúa con el jugador y coordina las herramientas disponibles:
  - `characterDB` para crear/buscar/borrar personajes.
  - `CombatAgent` para simular combates.
  - `Reglas KNAVE` para consultar el sistema de juego (usando RAG).

### 📦 2. Microservicio de creación de personajes
- Desplegado en Heroku y programado en Python con FastAPI.
- Expone un endpoint POST `/create-character` que recibe un nombre y devuelve un personaje completo según las reglas de Knave.
- Se conecta desde N8N mediante `HTTP Request` en el flujo "Character flow".

### 🔄 3. Workflows en N8N

#### `Hackaton main`
- Entrada vía Webhook.
- Agente "Señor oscuro" guía toda la partida.
- Usa herramientas auxiliares para:
  - Memoria contextual (`Window Buffer Memory`)
  - `characterDB` (toolWorkflow conectado a "Character flow")
  - `CombatAgent` (toolWorkflow para combate)
  - `Reglas KNAVE` (toolVectorStore con Supabase + bge-large embeddings + llama3.2)

#### `Character flow`
- Permite:
  - Crear personaje (llamando al microservicio).
  - Guardar resultado en Airtable `characterDB`.
  - Buscar personaje existente por nombre.
  - Borrar personaje existente.

#### `Combat Agent`
- Herramienta que simula el combate completo.
- Usa:
  - `characterDB` (toolWorkflow para traer datos del jugador)
  - `monsterDB` (consulta directa en Airtable)
  - GPT-4 como motor de ejecución del combate, con instrucciones específicas tipo "[COMBATE]...[/COMBATE]".

#### `Hackaton RAG document`
- Automatiza la carga de documentos PDF (como las reglas de Knave) al vector store en Supabase.
- Usa embeddings `bge-large` y segmentación por bloques (`RecursiveCharacterTextSplitter`).

#### `Monster scrap`
- Automatiza la extracción de monstruos desde el bestiario OSR.
- Recorre enlaces, scrapea datos y los adapta al formato Knave (HP = HD × 4).
- Inserta resultados en `monsterDB` de Airtable.

---

### 📊 4. Base de datos Airtable

#### `characterDB`
Almacena atributos del personaje, equipo, características y JSON original.

#### `monsterDB`
Contiene monstruos con estadísticas adaptadas (desde OSR → Knave).

---

### 💾 5. Vector Store (RAG)
- Almacenado en Supabase.
- Insertado mediante el flujo `Hackaton RAG document`.
- Consultado por el nodo `toolVectorStore` para dar contexto al agente GM.

---

### 🧠 Modelos utilizados
- **Agente Principal:** `GPT-4`
- **RAG:** `llama3.2` como modelo de respuesta, `bge-large` para embeddings

---

### 💻 Interfaz
- Entrada por Webhook local (simulado como frontend).
- Backend local o en la nube (Uvicorn para microservicio, N8N para lógica).

