# 💡 Registro Global de Notas, Tips y Conexiones de Herramientas

Este archivo recopila detalladamente todas las notas, tips técnicos, configuraciones de entorno y resoluciones de problemas generados en las sesiones con **Antigravity AI**, conectándolos con las herramientas del sistema y los repositorios asociados.

---

## 🛠️ Herramientas y Repositorios Conectados

- **Repositorio de Registro:** [Tavo-Ke/antigravity-sugerencias](https://github.com/Tavo-Ke/antigravity-sugerencias)
- **Sistema Operativo:** Windows
- **Entorno de Ejecución:** PowerShell / Node.js (`v22.14.0`), npm (`10.9.2`)
- **Graphify CLI:** `@nodesify/graphify` (`v0.8.0`)
- **Integración con GitHub API:** Token de Acceso Personal (PAT Classic) con ámbito `repo`
- **Configuración MCP Local:** `C:\Users\user\.gemini\config\mcp_config.json`

---

## 📚 Historial de Notas y Tips Registrados

### 📌 1. Solución a Bloqueo de Scripts `npm` en PowerShell
- **Categoría:** 🛠️ Configuración de Entorno / Troubleshooting
- **Herramientas Afectadas:** `PowerShell`, `Node.js`, `npm`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`SUGERENCIAS.md`)
- **Descripción:** Al intentar ejecutar `npm` directamente en PowerShell en Windows, puede aparecer un error de seguridad `PSSecurityException` indicando que la ejecución de scripts está deshabilitada en el sistema (`ExecutionPolicy`).
- **Solución:** `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` o `npm.cmd`.

---

### 📌 2. Configuración Segura de Tokens de GitHub (PAT) para Integraciones MCP
- **Categoría:** 🔑 Seguridad y Credenciales
- **Herramientas Afectadas:** `GitHub REST API`, `Antigravity MCP GitHub Server`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`SUGERENCIAS.md`)
- **Descripción:** Aplicar principio de menor privilegio seleccionando únicamente el ámbito `repo`.

---

### 📌 3. Persistencia de Memoria y Reglas Personalizadas
- **Categoría:** 💡 Tips & Mejores Prácticas
- **Herramientas Afectadas:** `Antigravity AI`, `System Rules`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`PROMPT_GUIA.md` / `SUGERENCIAS.md`)
- **Descripción:** Uso del comando `/learn` y reglas personalizadas en `.agents/rules/`.

---

### 📌 4. Instalación y Uso de Graphify (`@nodesify/graphify`)
- **Categoría:** 📦 Instalaciones & Procesos
- **Herramientas Afectadas:** `Node.js`, `npm`, `Graphify CLI`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`procesos/INSTALACIONES_Y_CONSULTAS.md`)
- **Descripción:** Instalación del paquete `@nodesify/graphify` para análisis de código y mapas de conocimiento.

---

### 📌 5. Exportación de Wikis y Árboles HTML Interactivos con Graphify
- **Categoría:** 🎨 Visualización & Documentación
- **Herramientas Afectadas:** `Graphify CLI`, `HTML`, `Markdown`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`procesos/INSTALACIONES_Y_CONSULTAS.md`)
- **Comandos de Exportación:**
  ```powershell
  npx @nodesify/graphify wiki   # Genera enciclopedia Markdown en .graphify/wiki/
  npx @nodesify/graphify tree   # Exporta arbol navegable en tree.html
  npx @nodesify/graphify export --format html # Grafo visual completo en graph.html
  ```
- **Resultado Esperado:** Mapas visuales interactivos navegables directamente desde el navegador web.

---

*Documento sincronizado y mantenido activamente en GitHub por Antigravity AI.*
