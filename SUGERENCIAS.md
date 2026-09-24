# 💡 Registro Global de Notas, Tips y Conexiones de Herramientas

Este archivo recopila detalladamente todas las notas, tips técnicos, configuraciones de entorno y resoluciones de problemas generados en las sesiones con **Antigravity AI**, conectándolos con las herramientas del sistema y los repositorios asociados.

---

## 🛠️ Herramientas y Repositorios Conectados

- **Repositorio de Registro:** [Tavo-Ke/antigravity-sugerencias](https://github.com/Tavo-Ke/antigravity-sugerencias)
- **Sistema Operativo:** Windows
- **Entorno de Ejecución:** PowerShell / Node.js (`v22.14.0`), npm (`10.9.2`)
- **Integración con GitHub API:** Token de Acceso Personal (PAT Classic) con ámbito `repo`
- **Configuración MCP Local:** `C:\Users\user\.gemini\config\mcp_config.json`

---

## 📚 Historial de Notas y Tips Registrados

### 📌 1. Solución a Bloqueo de Scripts `npm` en PowerShell
- **Categoría:** 🛠️ Configuración de Entorno / Troubleshooting
- **Herramientas Afectadas:** `PowerShell`, `Node.js`, `npm`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`SUGERENCIAS.md`)
- **Descripción:** Al intentar ejecutar `npm` directamente en PowerShell en Windows, puede aparecer un error de seguridad `PSSecurityException` indicando que la ejecución de scripts está deshabilitada en el sistema (`ExecutionPolicy`).
- **Soluciones:**
  - *Opción A (Permitir scripts firmados en usuario actual):*
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
  - *Opción B (Ejecutar binario cmd):*
    ```powershell
    npm.cmd -v
    ```
- **Resultado Esperado:** Ejecución limpia de comandos `npm` sin bloqueos de permisos.

---

### 📌 2. Configuración Segura de Tokens de GitHub (PAT) para Integraciones MCP
- **Categoría:** 🔑 Seguridad y Credenciales
- **Herramientas Afectadas:** `GitHub REST API`, `Antigravity MCP GitHub Server`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`SUGERENCIAS.md`)
- **Descripción:** Al configurar integraciones automáticas entre herramientas AI y GitHub, es crucial seguir el principio de menor privilegio.
- **Solución / Tip:**
  - En lugar de marcar todos los permisos (que exponen borrado de repositorios o datos personales), selecciona únicamente el permiso principal **`repo`** (Full control of private/public repositories).
  - El token se registra en `C:\Users\user\.gemini\config\mcp_config.json` bajo la variable `"GITHUB_PERSONAL_ACCESS_TOKEN"`.
- **Resultado Esperado:** Autenticación exitosa para crear repositorios y archivos manteniendo la cuenta protegida.

---

### 📌 3. Persistencia de Memoria y Reglas Personalizadas
- **Categoría:** 💡 Tips & Mejores Prácticas
- **Herramientas Afectadas:** `Antigravity AI`, `System Rules`
- **Repositorio:** `Tavo-Ke/antigravity-sugerencias` (`PROMPT_GUIA.md` / `SUGERENCIAS.md`)
- **Descripción:** Para guardar preferencias de entorno, hábitos o instrucciones de manera permanente entre diferentes chats y proyectos.
- **Solución / Tip:**
  - Utiliza el comando `/learn` dentro de la interfaz de chat para guardar un hábito o regla aprendida.
  - O crea archivos de reglas dentro de la carpeta `.agents/rules/` de tu proyecto o en la configuración global.
- **Resultado Esperado:** La IA recordará automáticamente el contexto y las preferencias en futuras sesiones.

---

*Documento sincronizado y mantenido activamente en GitHub por Antigravity AI.*
