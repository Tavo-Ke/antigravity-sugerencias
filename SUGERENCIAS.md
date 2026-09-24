# 💡 Registro de Sugerencias y Recomendaciones

Este archivo contiene el historial de sugerencias técnicas y recomendaciones generadas por Antigravity AI durante las sesiones de desarrollo.

---

## 📅 Registro de Sugerencias

### 1. Configuración de Entorno Node.js en Windows
- **Fecha:** 24 de septiembre de 2026
- **Contexto:** Verificación e instalación de Node.js / npm en Windows PowerShell.
- **Sugerencia:**
  - Node.js 22.14.0 y npm 10.9.2 están correctamente instalados.
  - Para evitar bloqueos por ExecutionPolicy en PowerShell, usar:
    `powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    `

### 2. Gestión de Seguridad en Tokens de GitHub (PAT)
- **Fecha:** 24 de septiembre de 2026
- **Contexto:** Autenticación para integración MCP de GitHub.
- **Sugerencia:**
  - Aplicar el principio de menor privilegio al generar Tokens de Acceso Personal (PAT).
  - Utilizar el ámbito de permisos epo para acceso a repositorios sin exponer permisos de administración de cuenta o de organización.

---

*Este documento se actualizará continuamente con nuevas recomendaciones de desarrollo.*