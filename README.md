# 🚀 Antigravity - Registro de Notas, Tips y Herramientas

¡Bienvenido! Este repositorio es la central de conocimientos donde **Antigravity AI** documenta automáticamente todas las notas, tips técnicos, soluciones de entorno y configuraciones de herramientas generadas en nuestras sesiones de desarrollo.

---

## 📌 Estructura del Repositorio

- 💡 [**SUGERENCIAS.md**](https://github.com/Tavo-Ke/antigravity-sugerencias/blob/main/SUGERENCIAS.md): El registro continuo de todas las notas, tips y soluciones ordenadas por categoría con sus herramientas asociadas.
- 🤖 [**PROMPT_GUIA.md**](https://github.com/Tavo-Ke/antigravity-sugerencias/blob/main/PROMPT_GUIA.md): El prompt de sistema y la directiva utilizada para documentar automáticamente.
- ⚙️ [**docs/AUTOMATIZACION.md**](https://github.com/Tavo-Ke/antigravity-sugerencias/blob/main/docs/AUTOMATIZACION.md): Explicación técnica de la arquitectura de automatización y funcionamiento interno.
- 📜 [**scripts/sync_sugerencias.ps1**](https://github.com/Tavo-Ke/antigravity-sugerencias/blob/main/scripts/sync_sugerencias.ps1): Script de PowerShell reutilizable para sincronizar notas vía GitHub REST API.

---

## 🛠️ Herramientas Conectadas

| Herramienta | Detalles / Versión | Propósito en el Sistema |
| :--- | :--- | :--- |
| **Node.js** | `v22.14.0` | Entorno de ejecución JavaScript local |
| **npm** | `10.9.2` | Gestor de paquetes de Node |
| **PowerShell** | `Windows` | Terminal y ejecución de scripts locales |
| **GitHub REST API** | `PAT Classic (scope: repo)` | Actualización y sincronización remota de notas |
| **Antigravity AI** | Assistant | Generación, estructuración y sincronización de tips |

---

## 📑 Categorías Registradas en `SUGERENCIAS.md`

1. 🛠️ **Configuración de Entorno & PowerShell:** Soluciones a políticas de ejecución (`ExecutionPolicy`) y ejecuciones de `npm`.
2. 🔑 **Seguridad & Credenciales:** Configuración de Tokens de GitHub con principio de menor privilegio (`repo`).
3. 💡 **Memoria & Reglas:** Uso del comando `/learn` y reglas personalizadas en `.agents/rules/`.

---

*Repositorio actualizado automáticamente por Antigravity AI.*
