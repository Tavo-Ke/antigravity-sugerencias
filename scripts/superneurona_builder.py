import os
import json
import re

VAULT_DIR = r"C:\Users\user\Documents\Obsidian Vault"

def analyze_vault():
    nodes_info = []
    tag_map = {}
    folder_map = {}
    
    for root, dirs, files in os.walk(VAULT_DIR):
        if any(skip in root for skip in [".obsidian", ".smart-env", ".graphify"]):
            continue
        for f in files:
            path = os.path.join(root, f)
            rel_path = os.path.relpath(path, VAULT_DIR)
            folder = os.path.dirname(rel_path) or "(Raíz)"
            
            if f.endswith(".md"):
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                        content = fp.read()
                        tags = re.findall(r"#([\w-]+)", content)
                        wikilinks = re.findall(r"\[\[(.*?)\]\]", content)
                        nodes_info.append({
                            "type": "file",
                            "file": rel_path.replace("\\", "/"),
                            "name": f.replace(".md", ""),
                            "folder": folder,
                            "tags": tags,
                            "links": wikilinks,
                            "size": len(content)
                        })
                        for t in tags:
                            tag_map.setdefault(t, []).append(rel_path)
                        folder_map.setdefault(folder, []).append(rel_path)
                except Exception as e:
                    pass
            elif f.endswith(".canvas"):
                nodes_info.append({
                    "type": "canvas",
                    "file": rel_path.replace("\\", "/"),
                    "name": f.replace(".canvas", ""),
                    "folder": folder
                })
    return nodes_info, folder_map, tag_map

def build_superneurona_canvas():
    canvas_path = os.path.join(VAULT_DIR, "SUPERNEURONA_HUB.canvas")
    
    # Coordinates layout: Central Superneurona at (0, 0)
    # Satellites orbiting around the center
    nodes = []
    edges = []
    
    # 1. CENTRAL SUPER-NEURON
    nodes.append({
        "id": "hub_central",
        "type": "text",
        "text": "# 🧠 SUPERNEURONA CENTRAL: HUB DEL CONOCIMIENTO\n\n**Bóveda Maestra de Aprendizaje e Inteligencia Contable**\n\n> *Punto neurálgico que interconecta todas las áreas: Ecuación Patrimonial, Elementos PCGE, NIIF, Casos Prácticos y Desarrollo Tecnológico.*\n\n---\n- 🎯 **Total de Conexiones Activas:** 8 Clústeres Temáticos\n- ⚖️ **Principio Rector:** Partida Doble & Causalidad Contable\n- 🚀 **Navegación:** Haz clic en los archivos o enlaces satélite para abrir cada dimensión.",
        "x": -250,
        "y": -150,
        "width": 600,
        "height": 340,
        "color": "6" # Morado / Púrpura central
    })

    # CLUSTERS DEFINITION:
    # 1. Ecuación y Ciclo Contable (Norte)
    # 2. Elementos del Activo (Noroeste)
    # 3. Pasivo y Patrimonio (Noreste)
    # 4. Gastos e Ingresos (Este)
    # 5. Marco Conceptual y NIIF (Oeste)
    # 6. Casos Prácticos y Panadería (Suroeste)
    # 7. Videos y Recursos Multimedia (Sur)
    # 8. Tecnología, IA y Código (Sureste)

    clusters = [
        {
            "id": "cl_ecuacion",
            "title": "⚖️ CLÚSTER 1: ECUACIÓN & CICLO CONTABLE",
            "text": "### ⚖️ Ecuación Fundamental & Ciclo\n- **Formula:** `Activo = Pasivo + Patrimonio`\n- **Fases del Proceso:**\n  1. 📝 Registrar (PCGE)\n  2. 🔍 Analizar (Integridad & Cuadre)\n  3. 📈 EEFF (Reportes NIIF)\n\n📂 **Archivos Clave:**\n- [[Desglose_Ecuacion_Contable]]\n- [[Diagrama_Ciclo_Contable]]\n- [[Contabilidad_Ecuacion_Contable/Sesion_10_Ecuacion_Contable]]",
            "x": -250,
            "y": -650,
            "width": 550,
            "height": 320,
            "color": "1", # Rojo/Coral
            "edge_color": "1"
        },
        {
            "id": "cl_activos",
            "title": "📦 CLÚSTER 2: ELEMENTOS DEL ACTIVO",
            "text": "### 📦 Activos: Bienes y Derechos\n- **Bienes:** Dinero (Cta 10), Mercaderías (Cta 20), Vehículos/Máquinas/Inmuebles (Cta 33).\n- **Derechos:** Cuentas por Cobrar (Cta 12), Préstamos (Cta 14), Reclamos (Cta 16).\n\n📂 **Vínculos:**\n- [[Contabilidad_Elementos_Activo/1_Teoria_Base]]\n- [[Contabilidad_Elementos_Activo/2_Caso_Auditoria]]\n- 🗺️ `Mapa_Activos.canvas`",
            "x": -950,
            "y": -550,
            "width": 500,
            "height": 300,
            "color": "5", # Azul cian
            "edge_color": "5"
        },
        {
            "id": "cl_pasivo_patrimonio",
            "title": "📑 CLÚSTER 3: PASIVO & PATRIMONIO",
            "text": "### 📑 Obligaciones: Terceros y Dueños\n- **Pasivo (Terceros):** CxP Proveedores (Cta 42), Deuda Financiera (Cta 45), Tributos SUNAT (Cta 40).\n- **Patrimonio (Dueños):** Capital Social (Cta 50), Acciones (Cta 51), Resultados Acumulados (Cta 59).\n\n📂 **Vínculos:**\n- [[Contabilidad_Pasivo_Patrimonio/1_Teoria_Base]]\n- [[Contabilidad_Pasivo_Patrimonio/2_Caso_Auditoria]]\n- 🗺️ `Mapa_Pasivo_Patrimonio.canvas`",
            "x": 480,
            "y": -550,
            "width": 500,
            "height": 300,
            "color": "2", # Naranja
            "edge_color": "2"
        },
        {
            "id": "cl_gastos_ingresos",
            "title": "📈 CLÚSTER 4: GASTOS, INGRESOS & NIIF 15",
            "text": "### 📈 Resultados Económicos\n- **Elemento 6:** Gastos por Naturaleza (Compras, Servicios, Cargas de Personal).\n- **Elemento 7:** Ingresos (Ventas de bienes y servicios).\n- **Elemento 8 y 9:** Cierre contable y Contabilidad Analítica de Explotación.\n\n📂 **Vínculos:**\n- [[Contabilidad_Gastos_Ingresos/1_Teoria_Base]]\n- [[Contabilidad_Gastos_Ingresos/5_Ensayo_NIIF15]]\n- 🗺️ `Mapa_Gastos_Ingresos.canvas`",
            "x": 580,
            "y": -120,
            "width": 500,
            "height": 320,
            "color": "3", # Amarillo
            "edge_color": "3"
        },
        {
            "id": "cl_marco_normativo",
            "title": "📚 CLÚSTER 5: MARCO CONCEPTUAL & NIIF",
            "text": "### 📚 Normativa y Principios Contables\n- **Marco Conceptual para la Información Financiera** (IASB)\n- **Características Cualitativas:** Relevancia, Representación Fiel, Comparabilidad, Verificabilidad, Oportunidad, Comprensibilidad.\n- **Políticas:** NIIF Plenas vs. NIIF para las PYMES.\n\n📂 **Vínculos:**\n- [[Contabilidad_Marco_Conceptual/Apuntes_Marco_Conceptual]]\n- [[Contabilidad_Principios_Sesion_04/1_Teoria_Base]]\n- 🗺️ `Mapa_Visual.canvas`",
            "x": -1000,
            "y": -120,
            "width": 520,
            "height": 320,
            "color": "4", # Verde
            "edge_color": "4"
        },
        {
            "id": "cl_casos_practicos",
            "title": "🥖 CLÚSTER 6: CASOS PRÁCTICOS & PANADERÍA DOMINGA",
            "text": "### 🥖 Aplicación Real: Casos de Negocio\n- **Caso Empresa:** Panadería Dominga\n- **Dinámica Aplicada:** Asientos de constitución, compras de insumos (harina/azúcar), ventas diarias con boleta/factura y liquidación de impuestos.\n\n📂 **Vínculos:**\n- [[Casos_Panaderia_Dominga/Caso_Panaderia_Dominga]]\n- 🗺️ `Canvas_Panaderia.canvas`",
            "x": -950,
            "y": 320,
            "width": 500,
            "height": 280,
            "color": "2", # Naranja
            "edge_color": "2"
        },
        {
            "id": "cl_multimedia_videos",
            "title": "🎬 CLÚSTER 7: VIDEOS & RECURSOS MULTIMEDIA",
            "text": "### 🎬 Videoteca y Recursos Interactivos\n\n> *Videos pedagógicos seleccionados integrables directamente en Obsidian:*  \n\n1. 🎥 **Ecuación Contable y la Partida Doble:**\n   https://www.youtube.com/watch?v=sB1j_c_1s3c\n2. 🎥 **Dinámica del Plan Contable (PCGE):**\n   https://www.youtube.com/watch?v=kYJv13Q2eZ4\n3. 🎥 **Elaboración de Estados Financieros:**\n   https://www.youtube.com/watch?v=8q2w2j5h4YI\n\n*💡 Consejo: Puedes pegar cualquier URL de YouTube en una nota de Obsidian para ver el reproductor integrado.*",
            "x": -250,
            "y": 320,
            "width": 600,
            "height": 340,
            "color": "1", # Rojo multimedia
            "edge_color": "1"
        },
        {
            "id": "cl_tecnologia_ia",
            "title": "🤖 CLÚSTER 8: TECNOLOGÍA, IA & CÓDIGO",
            "text": "### 🤖 Herramientas Digitales & Programación\n- **LangGraph:** Orquestación de grafos cognitivos y multi-agentes.\n- **Python & OOP:** Automatizaciones de datos y scripts de análisis.\n- **VS Code Agents & MCP:** Herramientas y protocolos de conexión de IA.\n\n📂 **Vínculos:**\n- [[📑 Verificación e Instalación de LangGraph en Windows]]\n- [[VS Code ahora tiene AGENTES ?? (y es ridículamente barato)]]\n- [[PYTHON]] / [[POO]]",
            "x": 480,
            "y": 320,
            "width": 520,
            "height": 300,
            "color": "5", # Azul
            "edge_color": "5"
        }
    ]

    for c in clusters:
        nodes.append({
            "id": c["id"],
            "type": "text",
            "text": c["text"],
            "x": c["x"],
            "y": c["y"],
            "width": c["width"],
            "height": c["height"],
            "color": c["color"]
        })
        edges.append({
            "id": f"edge_hub_to_{c['id']}",
            "fromNode": "hub_central",
            "fromSide": "bottom" if c["y"] > 0 else ("top" if c["y"] < -200 else ("left" if c["x"] < 0 else "right")),
            "toNode": c["id"],
            "toSide": "top" if c["y"] > 0 else ("bottom" if c["y"] < -200 else ("right" if c["x"] < 0 else "left")),
            "color": c["edge_color"]
        })

    # Inter-cluster synaptic connections (e.g. Ecuacion -> Activos, Ecuacion -> Pasivos, Activos -> Casos)
    synaptic_edges = [
        ("cl_ecuacion", "cl_activos", "5", "left", "right"),
        ("cl_ecuacion", "cl_pasivo_patrimonio", "2", "right", "left"),
        ("cl_activos", "cl_casos_practicos", "4", "bottom", "top"),
        ("cl_pasivo_patrimonio", "cl_gastos_ingresos", "3", "bottom", "top"),
        ("cl_marco_normativo", "cl_ecuacion", "4", "top", "left"),
        ("cl_multimedia_videos", "cl_ecuacion", "1", "top", "bottom"),
    ]
    for idx, (f, t, col, fs, ts) in enumerate(synaptic_edges):
        edges.append({
            "id": f"synapse_{idx}",
            "fromNode": f,
            "fromSide": fs,
            "toNode": t,
            "toSide": ts,
            "color": col
        })

    canvas_data = {
        "nodes": nodes,
        "edges": edges
    }

    with open(canvas_path, "w", encoding="utf-8") as fp:
        json.dump(canvas_data, fp, indent=2, ensure_ascii=False)
    
    print(f"Canvas creado con éxito en: {canvas_path}")
    return canvas_path

def build_superneurona_markdown(nodes_info, folder_map, tag_map):
    md_path = os.path.join(VAULT_DIR, "SUPERNEURONA_CENTRAL.md")
    
    lines = [
        "# 🧠 SUPERNEURONA CENTRAL: MATRIZ DE CONEXIÓN TOTAL",
        "",
        "> **Bóveda:** Obsidian Vault | **Nodo:** Cerebro Principal",
        "> Esta superneurona unifica automáticamente todas las notas, mapas visuales (`.canvas`), ecuaciones, casos prácticos y videos en una sola red sináptica.",
        "",
        "---",
        "",
        "## 🌌 1. Acceso Rápido al Mega Canvas Visual",
        "",
        "- 🗺️ **Abre el Mapa Neuronal 2D en Obsidian:** [[SUPERNEURONA_HUB.canvas]]",
        "- 📊 **Canvas Específicos:**",
        "  - [[Ciclo_Contable_Ecuacion.canvas]]",
        "  - [[Desglose_Ecuacion_Contable.canvas]]",
        "  - [[Casos_Panaderia_Dominga/Canvas_Panaderia.canvas]]",
        "  - [[Contabilidad_Gastos_Ingresos/Mapa_Gastos_Ingresos.canvas]]",
        "  - [[Contabilidad_Marco_Conceptual/Mapa_Visual.canvas]]",
        "  - [[Contabilidad_Elementos_Activo/Mapa_Activos.canvas]]",
        "  - [[Contabilidad_Pasivo_Patrimonio/Mapa_Pasivo_Patrimonio.canvas]]",
        "",
        "---",
        "",
        "## ⚖️ 2. Núcleo Contable Fundamental",
        "",
        "$$\\text{ACTIVO} = \\text{PASIVO} + \\text{PATRIMONIO}$$",
        "",
        "| Elemento | Naturaleza | Cuentas PCGE Principales | Notas de la Bóveda |",
        "| :--- | :--- | :--- | :--- |",
        "| **Activo** | Bienes (tangibles/intangibles) y Derechos por cobrar | Elemento 1 (Cta 10, 12), Elemento 2 (Cta 20), Elemento 3 (Cta 33) | [[Desglose_Ecuacion_Contable]], [[Contabilidad_Elementos_Activo/1_Teoria_Base]] |",
        "| **Pasivo** | Obligaciones con Terceros (Proveedores, Bancos, SUNAT) | Elemento 4 (Cta 40, 42, 45) | [[Contabilidad_Pasivo_Patrimonio/1_Teoria_Base]], [[Contabilidad_Pasivo_Patrimonio/2_Caso_Auditoria]] |",
        "| **Patrimonio** | Obligaciones con los Dueños (Aportes y Ganancias) | Elemento 5 (Cta 50, 59) | [[Contabilidad_Sesion_09_Activo_Pasivo_Patrimonio]], [[Contabilidad_Pasivo_Patrimonio/1_Teoria_Base]] |",
        "| **Resultados** | Gastos e Ingresos del Periodo | Elemento 6 (Gastos), Elemento 7 (Ingresos) | [[Contabilidad_Gastos_Ingresos/1_Teoria_Base]], [[Contabilidad_Gastos_Ingresos/5_Ensayo_NIIF15]] |",
        "",
        "---",
        "",
        "## 🎬 3. Videoteca y Recursos Multimedia Integrados",
        "",
        "### 🎥 Video 1: La Ecuación Contable Explicada con Manzanas",
        "`youtube: https://www.youtube.com/watch?v=sB1j_c_1s3c`",
        "",
        "### 🎥 Video 2: Dinámica del Plan Contable General Empresarial (PCGE)",
        "`youtube: https://www.youtube.com/watch?v=kYJv13Q2eZ4`",
        "",
        "### 🎥 Video 3: Los 4 Estados Financieros Básicos bajo NIIF",
        "`youtube: https://www.youtube.com/watch?v=8q2w2j5h4YI`",
        "",
        "---",
        "",
        "## 🧭 4. Directorio de Carpetas y Nodos Conectados",
        ""
    ]
    
    for folder, files in sorted(folder_map.items()):
        if folder == "(Raíz)":
            continue
        lines.append(f"### 📂 `{folder}` ({len(files)} notas)")
        for fl in files[:6]:
            name = os.path.basename(fl).replace(".md", "")
            lines.append(f"- [[{fl.replace('.md', '')}|{name}]]")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 🏷️ 5. Nube de Etiquetas Semánticas (Top Tags)",
        ""
    ])
    
    top_tags = sorted(tag_map.items(), key=lambda x: len(x[1]), reverse=True)[:15]
    for tag, note_list in top_tags:
        lines.append(f"- **#{tag}** ({len(note_list)} notas relacionadas)")

    lines.append("\n*Creado automáticamente por el generador neuronal de Antigravity AI.*")

    with open(md_path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines))
    print(f"Nota Maestra creada con éxito en: {md_path}")
    return md_path

if __name__ == "__main__":
    nodes, folders, tags = analyze_vault()
    print(f"Nodos escaneados: {len(nodes)}")
    build_superneurona_canvas()
    build_superneurona_markdown(nodes, folders, tags)
