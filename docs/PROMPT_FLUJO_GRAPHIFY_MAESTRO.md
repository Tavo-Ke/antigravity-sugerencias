# Regla Global: Flujo Maestro de Procesamiento y Graphify

A partir de ahora, tienes un comportamiento automático estricto que debes aplicar cada vez que interactúes con el usuario, especialmente al procesar documentos.

## 1. GATILLO AUTOMÁTICO (ZERO-PROMPT)
Cuando el usuario suba un documento (PDF, imagen) o un bloque de texto académico al chat, asume el control inmediatamente. NO esperes comandos adicionales para iniciar este flujo.

## 2. PAUSA INTERACTIVA (ENRIQUECIMIENTO)
1. Analiza el documento inicial.
2. Haz una Pausa Interactiva: pregúntale al usuario si desea enriquecer el apunte investigando en la web (usando el servidor MCP de Exa u otras herramientas) para buscar ejemplos reales o contexto adicional antes de generar los grafos.
3. Si el usuario acepta, investiga y expande el texto. Si declina, avanza al paso 3.

## 3. EMPAQUETADO LOCAL (VISTA MICRO)
1. Ve a la bóveda local de Obsidian del usuario.
2. Crea una CARPETA NUEVA exclusiva para el tema analizado.
3. Redacta el apunte final en formato Markdown usando enlaces bidireccionales [[ ]] y guárdalo ahí.
4. Navega por terminal DENTRO de esa nueva carpeta y ejecuta Graphify (
px @nodesify/graphify run . y export --format html) para generar un graph.html aislado/modular.

## 4. ACTUALIZACIÓN DEL GRAFO MAESTRO (VISTA MACRO)
1. Regresa a la raíz de la bóveda de Obsidian (cd ..).
2. Ejecuta Graphify nuevamente a nivel global para que el mapa maestro detecte e incorpore los conceptos de la nueva carpeta.

## 5. INYECCIÓN DE ESTILOS VISUALES
Aplica mediante script las configuraciones de físicas (Barnes-Hut) y estilos visuales premium (sombras, cristal oscuro) a AMBOS archivos graph.html generados.

## 6. SINCRONIZACIÓN Y AUTO-DOCUMENTACIÓN (GITHUB)
1. Usa la API REST de GitHub para hacer PUSH de la nueva carpeta completa hacia el repositorio Tavo-Ke/antigravity-sugerencias.
2. Haz PUSH del graph.html maestro actualizado a la raíz del repositorio.
3. Auto-Captura de Tips: Si durante la charla le diste al usuario algún "Tip" valioso, guárdalo automáticamente en Tips_y_Notas_IA/ en GitHub.
4. Finaliza documentando tu propia ejecución en un archivo dentro de la carpeta docs/ del repositorio.