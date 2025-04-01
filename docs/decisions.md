# Justificación de elecciones tecnológicas

## Modelos de IA

- **GPT-4 (OpenAI)**: Inicialmente, el proyecto se diseñó para funcionar completamente en local, utilizando llama3.2 como modelo principal con Ollama. Sin embargo, durante las pruebas iniciales, se observó un comportamiento inconsistente del agente: no seguía las instrucciones del prompt de manera confiable y en ocasiones ignoraba partes críticas del flujo. A pesar de múltiples ajustes en la temperatura, sistema message y estructura del prompt, no se logró una ejecución robusta.

Tras migrar a GPT-4, todos los flujos comenzaron a comportarse como se esperaba. El agente fue capaz de seguir prompts complejos, usar correctamente herramientas y mantener coherencia durante largos turnos de conversación. Por esta razón, se decidió utilizar GPT-4 como modelo principal del Agente Game Master, garantizando estabilidad y fluidez narrativa.
- **llama3.2**: Usado como modelo de respuesta en el vector store, debido a su eficiencia y rendimiento en entorno local.
- **bge-large**: Seleccionado para embeddings por su equilibrio entre precisión semántica y eficiencia computacional.

## Base de Datos

- **Airtable**: Proporciona una solución gratuita, rápida de integrar y suficiente para el alcance del proyecto. Se ha utilizado para guardar tanto los personajes como los enemigos.

## Microservicio

- **Python + FastAPI**: Ideal para construir un endpoint ligero, rápido y bien documentado. Uvicorn como servidor ASGI para ejecución local.

## Entorno

- **N8N autoalojado**: Permite control total del flujo, integración de APIs, parsing de respuestas, almacenamiento temporal y lógica condicional sin necesidad de escribir código explícito.
