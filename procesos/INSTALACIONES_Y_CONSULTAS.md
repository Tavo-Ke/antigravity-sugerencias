# 🛠️ Registro de Procesos, Consultas e Instalaciones

Este documento forma parte de la carpeta `procesos/` y sirve como bitácora detallada de todas las instalaciones de software, consultas ejecutadas y procesos del sistema realizados por **Antigravity AI**.

---

## 📦 1. Registro de Instalaciones Realizadas

### 📌 Instalación de Graphify (`@nodesify/graphify`)
- **Fecha:** 24 de septiembre de 2026
- **Paquete NPM:** `@nodesify/graphify` (`v0.8.0`)
- **Comando de Instalación:**
  ```powershell
  npm install -g @nodesify/graphify
  ```
- **Verificación y Prueba de Ejecución:**
  ```powershell
  npx @nodesify/graphify --help
  ```
- **Propósito y Utilidad:**
  Permite transformar cualquier directorio o proyecto de código en un gráfico de conocimiento (*Knowledge Graph*), ofreciendo consultas AST, análisis de dependencias, exportación a HTML/GraphML y servidores MCP para agentes AI.

---

## 🔍 2. Auditoría de Consultas y Comandos Ejecutados

| Fecha | Herramienta / CLI | Comando Ejecutado | Resultado |
| :--- | :--- | :--- | :--- |
| 24/09/2026 | `Node.js / npm` | `node -v; npm -v` | Detectado Node `v22.14.0`, npm `10.9.2`. |
| 24/09/2026 | `npm` | `npm install -g @nodesify/graphify` | Instalación global completada exitosamente. |
| 24/09/2026 | `Graphify CLI` | `npx @nodesify/graphify run "limites_y_continuidad"` | Generación de gráfico de conocimiento (24 nodos y 21 aristas en 7 comunidades). |
| 24/09/2026 | `Graphify CLI` | `npx @nodesify/graphify wiki` | Exportación de 17 artículos de Wikipedia en `.graphify/wiki`. |
| 24/09/2026 | `Graphify CLI` | `npx @nodesify/graphify tree` | Exportación de árbol HTML navegable en `tree.html`. |
| 24/09/2026 | `Graphify CLI` | `npx @nodesify/graphify export --format html` | Exportación de grafo visual en `graph.html`. |
| 24/09/2026 | `PowerShell` | `Invoke-RestMethod (GitHub API)` | Sincronización automática de archivos en GitHub. |

---

## 🌐 3. Caso Práctico: Grafo de Conocimiento y Ejercicios Resueltos

Se estructuraron las notas y la guía de ejercicios del capítulo de Matemáticas I en la carpeta `limites_y_continuidad/`:
- `01_concepto_de_limite.md`
- `02_calculo_de_limites.md`
- `03_continuidad_de_funciones.md`
- `04_ejercicios_resueltos_capitulo7.md`

### Resultados de Graphify:
- **Nodos agregados:** 24
- **Aristas (Edges):** 21
- **Comunidades de conocimiento:** 7
- **Eficiencia de consulta:** 1.8x Token Reduction.
- **Visualización:** Wiki Markdown (17 artículos) y Árboles HTML (`tree.html` / `graph.html`).
