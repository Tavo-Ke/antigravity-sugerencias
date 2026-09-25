# 🧪 Entorno Experimental (Sandbox Mode)

Bienvenido a la rama experimental-features. Este espacio fue creado como un "Sandbox" (Caja de arena) para probar automatizaciones avanzadas, integraciones con Obsidian y flujos de Graphify sin poner en riesgo la estabilidad del proyecto principal (main).

## 🏗️ Arquitectura: El Puente API (Cero-Git Local)
A diferencia de los entornos de desarrollo tradicionales, este espacio funciona con una arquitectura **API Bridge**. 

* **El Problema:** La bóveda local de Obsidian del usuario no está inicializada como un repositorio Git local (.git). Exigir comandos manuales rompe la automatización.
* **La Solución:** La Inteligencia Artificial actúa como un puente directo. Extrae los archivos locales de Obsidian, los codifica en Base64, y utiliza la **API REST de GitHub** para inyectarlos directamente en esta rama en la nube.

## ⚙️ ¿Cómo se construyó? (Flujo Técnico)
1. **Extracción de SHA:** La IA consultó el endpoint GET /repos/{owner}/{repo}/git/refs/heads/main para obtener la firma exacta del último estado de producción.
2. **Creación de Rama:** Se envió un POST /repos/{owner}/{repo}/git/refs para crear efs/heads/experimental-features partiendo de ese SHA.
3. **Enrutamiento:** La IA ajustó sus scripts internos de PowerShell. Ahora, cada petición PUT incluye el parámetro "branch": "experimental-features".

## 🚀 Próximos Pasos (Experimentos en Cola)
En esta rama se desarrollarán y probarán las siguientes características antes de pasarlas a producción:
- [ ] **Evolución A:** Dashboard Web Interactivo para navegar por múltiples grafos.
- [ ] **Evolución B:** Inyección de Metadatos YAML y consultas dinámicas con Dataview.
- [ ] **Evolución C:** Generación de mapas mentales visuales automatizados usando Obsidian Canvas vía MCP.

---
*Documento generado y subido automáticamente por el sistema Antigravity.*