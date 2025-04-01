# Hackaton Game Master 🎲🧙‍♂️

**Participante:** Luis  
**Correo de contacto:** lurodri93@gmail.com

## Descripción del proyecto

**Hackaton Game Master** es una plataforma de rol asistida por IA diseñada para partidas en solitario utilizando el sistema de reglas **Knave**. El proyecto fue desarrollado para el Hackatón con el objetivo de integrar múltiples tecnologías de IA y automatización para simular un *Game Master* (GM) digital capaz de generar personajes, gestionar combates y guiar aventuras completas sin intervención humana.

Desde su concepción, el enfoque fue construir una solución híbrida, con **componentes locales y en la nube**, capaz de aprovechar lo mejor de ambos entornos. Inicialmente planteado para funcionar con modelos locales (`llama3.2`), el proyecto evolucionó tras detectar limitaciones de seguimiento de instrucciones, y finalmente se integró con `GPT-4`, lo cual resolvió todos los problemas de consistencia en el comportamiento del agente.

---

## Funcionalidades clave

- 👤 **Creación de personajes dinámica** desde un microservicio en Python, siguiendo las reglas de Knave.
- 🧠 **Agente Game Master con GPT-4** que guía al jugador, propone aventuras y resuelve mecánicas usando herramientas de N8N.
- ⚔️ **Combates automáticos** simulados por un agente técnico que respeta los turnos, tiradas y moral de los enemigos.
- 📚 **RAG sobre reglas del sistema**, cargando el manual de Knave y permitiendo al GM consultar información precisa durante la partida.
- 👹 **Scraping y adaptación de enemigos** desde un bestiario OSR, transformados automáticamente al sistema Knave.
- 🗃️ **Persistencia en Airtable** para guardar personajes, monstruos y facilitar la continuidad de las partidas.

---

## Tecnologías utilizadas

- **Modelos de IA:** GPT-4 (OpenAI), llama3.2 (RAG), bge-large (embeddings)
- **Vector Store:** Supabase
- **Automatización:** N8N autoalojado
- **Base de datos:** Airtable
- **Microservicio:** FastAPI + Uvicorn en Heroku
- **Frontend:** Simulado mediante Webhook en local

---

Este proyecto demuestra cómo un entorno low-code puede integrarse eficazmente con herramientas avanzadas de IA para crear experiencias inmersivas y personalizadas.
