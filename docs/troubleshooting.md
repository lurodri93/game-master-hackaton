# Posibles errores y cómo solucionarlos

## Error: No se genera personaje
**Causa probable**: El microservicio no está activo.
**Solución**: Asegúrate de que el servidor Uvicorn esté corriendo (`uvicorn app:app --reload`).

## Error: No se puede acceder a Airtable
**Causa probable**: API Key incorrecta o base incorrectamente referenciada.
**Solución**: Revisa tu API Key de Airtable, la base debe llamarse "Hackaton" y las tablas "characterDB" y "monsterDB".

## Error: El agente de IA responde de forma incoherente
**Causa probable**: Error en el prompt inicial.
**Solución**: Revisa los prompts en la carpeta `/prompts/`, especialmente que el agente tenga acceso a las reglas de Knave y ejemplos claros.

## Error: Vector store no devuelve contexto
**Causa probable**: Problemas en la indexación con `bge-large`.
**Solución**: Verifica que los embeddings se generen correctamente y que el modelo `llama3.2` esté consultando bien la base de vectores.

## Error: Enemigo no adaptado correctamente
**Causa probable**: HD no transformado a HP.
**Solución**: Verifica que `HP = HD x 4` o `HD x 5` según dificultad deseada.
