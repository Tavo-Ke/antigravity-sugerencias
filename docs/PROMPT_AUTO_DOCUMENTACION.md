# Prompt de Auto-Documentación (Regla de Sistema)

Este es el prompt (o instrucción de sistema) diseñado para que la Inteligencia Artificial automatice la documentación de cualquier tarea técnica sin que tengas que pedírselo cada vez.

---

## 🤖 El Prompt (Instrucción para la IA)

Copia y pega este texto como una regla global para tu asistente, o envíalo al inicio de una nueva conversación:

> **REGLA DE COMPORTAMIENTO: AUTO-DOCUMENTACIÓN ACTIVA**
> 
> A partir de ahora, cada vez que te pida configurar una nueva herramienta (ejemplo: instalar Obsidian, conectar GitHub Actions, configurar Graphify, etc.) o cuando resolvamos un problema técnico complejo juntos, debes realizar un paso final obligatorio antes de dar por terminada la tarea:
> 
> **Debes crear (o actualizar) automáticamente un archivo Markdown en la carpeta `docs/` del proyecto explicando exactamente qué hiciste.**
> 
> El documento generado debe contener:
> 1. **Objetivo:** Qué me pidió el usuario.
> 2. **Comandos utilizados:** Qué instalaste o ejecutaste en la terminal (ej. `npm install...`, comandos de Git).
> 3. **Archivos modificados/creados:** Qué configuraciones cambiaste y por qué.
> 4. **Cómo funciona:** Una explicación breve para que el usuario entienda cómo usar lo que acabas de configurar.
> 
> **No me preguntes si quiero que lo documentes. Simplemente genera el archivo en `docs/` y avísame en el chat que ya quedó registrado.**

---

## 💡 ¿Por qué usar este prompt?
Al proporcionarle esta instrucción a la IA, te aseguras de que tu repositorio siempre tenga una "memoria fotográfica". Así, si en 6 meses olvidas cómo configuramos el servidor MCP de Obsidian o el bot de Graphify, tendrás un manual paso a paso redactado a tu medida en la carpeta `docs/`.
