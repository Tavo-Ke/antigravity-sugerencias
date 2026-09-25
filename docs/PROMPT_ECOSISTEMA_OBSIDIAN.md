# Guía y Prompt para Ecosistemas Inteligentes (Obsidian + Graphify + GitHub + MCP)

Este documento guarda un registro del ecosistema automatizado que construimos y proporciona un **Prompt Estructurado** para que puedas replicarlo instantáneamente en el futuro con cualquier otra Inteligencia Artificial o en nuevos proyectos.

---

## 🏗️ La Arquitectura del Ecosistema

Lo que construimos fue un flujo de 4 niveles:
1. **Creación (Obsidian):** Redacción local usando enlaces bidireccionales `[[ ]]`.
2. **Puente Local (MCP Server):** Un servidor que expone la bóveda a la IA para lectura/escritura en tiempo real.
3. **Automatización (GitHub Actions):** Un robot en la nube que detecta cambios.
4. **Procesamiento y Visualización (Graphify):** Generación automática del mapa conceptual interactivo.

---

## 💬 El Prompt Estructurado (Copia y Pega)

Cuando quieras que una IA te configure todo este sistema desde cero en un nuevo repositorio, usa la siguiente estructura de prompt:

> **Rol:** Eres un Ingeniero de Software experto en DevOps, Knowledge Management y automatización con Graphify.
> 
> **Objetivo:** Quiero configurar un ecosistema de apuntes automatizado para mi repositorio en GitHub usando Obsidian, Graphify y GitHub Actions.
> 
> **Instrucciones paso a paso:**
> 1. **Archivos de Configuración:** Genera un script en Node.js llamado `scripts/apply_styles.js` que tome el archivo `graph.html` generado por Graphify y le inyecte físicas (Barnes-Hut, gravedad central 0.1), fondos oscuros con gradientes, bordes translúcidos y sombras a los nodos.
> 2. **GitHub Actions:** Crea un archivo `.github/workflows/graphify.yml` que se active al hacer `push` de archivos `.md`. El bot debe:
>    - Usar Node 20.
>    - Ejecutar `npx @nodesify/graphify run .` y `npx @nodesify/graphify export --format html`.
>    - Ejecutar el script `apply_styles.js`.
>    - Hacer commit de vuelta al repositorio con `stefanzweifel/git-auto-commit-action@v5`.
> 3. **Conexión MCP:** Dame las instrucciones exactas para configurar el archivo `mcp_config.json` de mi sistema con el puerto e información del "Obsidian MCP Connector" para que puedas leer mi bóveda localmente mediante SSE.
> 4. Sube los scripts (`apply_styles.js` y `graphify.yml`) usando la API REST de GitHub. Si hay error por permisos de *workflow*, dame el código para que yo lo copie manualmente.
> 5. Crea un archivo vacío `tree.html` en la raíz si es necesario para evitar fallos de pathspec en el bot de GitHub.

---

## 🛠️ Notas Técnicas para el Usuario
* **Errores 404 en GitHub Actions:** Si la IA no puede subir el archivo `.yml`, recuerda que los Personal Access Tokens (PAT) necesitan el permiso `workflow` explícitamente marcado.
* **Error 128 en el Commit del Bot:** Si el bot falla al hacer commit porque no encuentra `tree.html` o algún otro archivo, asegúrate de que el `file_pattern` del Action coincida exactamente con los archivos que se generan, o crea archivos "dummy" (vacíos) en la raíz para que no colapse.
* **Recarga de MCP:** Siempre que agregues un token de Obsidian al archivo `mcp_config.json`, la IA necesitará reiniciar su sesión para cargar las herramientas.
