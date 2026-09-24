# ðŸ’¡ Registro Global de Notas, Tips y Conexiones de Herramientas

Este archivo recopila detalladamente todas las notas, tips tÃ©cnicos, configuraciones de entorno y resoluciones de problemas generados en las sesiones con **Antigravity AI**, conectÃ¡ndolos con las herramientas del sistema y los repositorios asociados.

---

## ðŸ› ï¸ Herramientas y Repositorios Conectados

- **Repositorio de Registro:** [Tavo-Ke/antigravity-sugerencias](https://github.com/Tavo-Ke/antigravity-sugerencias)
- **Sistema Operativo:** Windows
- **Entorno de EjecuciÃ³n:** PowerShell / Node.js (22.14.0), npm (10.9.2)
- **IntegraciÃ³n con GitHub API:** Token de Acceso Personal (PAT Classic) con Ã¡mbito epo
- **ConfiguraciÃ³n MCP Local:** C:\Users\user\.gemini\config\mcp_config.json

---

## ðŸ“š Historial de Notas y Tips Registrados

### ðŸ“Œ 1. SoluciÃ³n a Bloqueo de Scripts 
pm en PowerShell
- **CategorÃ­a:** ðŸ› ï¸ ConfiguraciÃ³n de Entorno / Troubleshooting
- **Herramientas Afectadas:** PowerShell, Node.js, 
pm
- **Repositorio:** Tavo-Ke/antigravity-sugerencias (SUGERENCIAS.md)
- **DescripciÃ³n:** Al intentar ejecutar 
pm directamente en PowerShell en Windows, puede aparecer un error de seguridad PSSecurityException indicando que la ejecuciÃ³n de scripts estÃ¡ deshabilitada en el sistema (ExecutionPolicy).
- **Soluciones:**
  - *OpciÃ³n A (Permitir scripts firmados en usuario actual):*
    `powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    `
  - *OpciÃ³n B (Ejecutar binario cmd):*
    `powershell
    npm.cmd -v
    `
- **Resultado Esperado:** EjecuciÃ³n limpia de comandos 
pm sin bloqueos de permisos.

---

### ðŸ“Œ 2. ConfiguraciÃ³n Segura de Tokens de GitHub (PAT) para Integraciones MCP
- **CategorÃ­a:** ðŸ”‘ Seguridad y Credenciales
- **Herramientas Afectadas:** GitHub REST API, Antigravity MCP GitHub Server
- **Repositorio:** Tavo-Ke/antigravity-sugerencias (SUGERENCIAS.md)
- **DescripciÃ³n:** Al configurar integraciones automÃ¡ticas entre herramientas AI y GitHub, es crucial seguir el principio de menor privilegio.
- **SoluciÃ³n / Tip:**
  - En lugar de marcar todos los permisos (que exponen borrado de repositorios o datos personales), selecciona Ãºnicamente el permiso principal **epo** (Full control of private/public repositories).
  - El token se registra en C:\Users\user\.gemini\config\mcp_config.json bajo la variable "GITHUB_PERSONAL_ACCESS_TOKEN".
- **Resultado Esperado:** AutenticaciÃ³n exitosa para crear repositorios y archivos manteniendo la cuenta protegida.

---

### ðŸ“Œ 3. Persistencia de Memoria y Reglas Personalizadas
- **CategorÃ­a:** ðŸ’¡ Tips & Mejores PrÃ¡cticas
- **Herramientas Afectadas:** Antigravity AI, System Rules
- **Repositorio:** Tavo-Ke/antigravity-sugerencias (PROMPT_GUIA.md / SUGERENCIAS.md)
- **DescripciÃ³n:** Para guardar preferencias de entorno, hÃ¡bitos o instrucciones de manera permanente entre diferentes chats y proyectos.
- **SoluciÃ³n / Tip:**
  - Utiliza el comando /learn dentro de la interfaz de chat para guardar un hÃ¡bito o regla aprendida.
  - O crea archivos de reglas dentro de la carpeta .agents/rules/ de tu proyecto o en la configuraciÃ³n global.
- **Resultado Esperado:** La IA recordarÃ¡ automÃ¡ticamente el contexto y las preferencias en futuras sesiones.

---

*Documento sincronizado y mantenido activamente en GitHub por Antigravity AI.*