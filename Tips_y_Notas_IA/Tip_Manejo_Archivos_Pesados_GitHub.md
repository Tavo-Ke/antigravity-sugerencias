# Tip: Manejo de Archivos Pesados en GitHub y Graphify

**Fecha:** 25 de septiembre de 2026
**Contexto:** Capturado automáticamente desde el chat de Antigravity.

Cuando se maneja un "Segundo Cerebro" o ecosistema con Obsidian y Graphify, los archivos muy pesados (como libros enteros en PDF, audios largos o videos) pueden romper la automatización. Aquí están los tips clave para solucionarlo:

### 1. Límite de 100 MB de GitHub
* **El Problema:** GitHub no permite subir archivos individuales que superen los 100 MB. Si Obsidian Git intenta sincronizar un PDF de 150 MB, el proceso completo fallará.
* **El Tip:** Crea un archivo .gitignore en la raíz de tu bóveda e incluye la línea *.pdf (o la ruta de la carpeta de libros) para que Git los ignore. Si realmente necesitas subirlos, debes instalar y configurar **Git LFS (Large File Storage)**.

### 2. Congelamiento de Graphify
* **El Problema:** Graphify puede quedarse sin memoria intentando procesar carpetas con miles de imágenes o archivos no textuales.
* **El Tip:** Crea un archivo .graphifyignore en la raíz de tu proyecto. Agrega las carpetas donde guardas imágenes, PDFs o recursos pesados. Así, Graphify solo se concentrará en las notas .md, haciéndolo rapidísimo.