# 📊 Diagrama del Ciclo y Ecuación Contable Fundamental

Este diagrama estructura y formaliza el contenido de la pizarra explicativa, integrando la **Ecuación Contable Fundamental** con las **tres fases operativas del ciclo contable peruano (PCGE)**.

---

## 📌 1. Representación en Diagrama de Flujo (Mermaid)

```mermaid
flowchart TD
    classDef main fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#ffffff,font-weight:bold;
    classDef step fill:#0f172a,stroke:#64748b,stroke-width:1.5px,color:#f8fafc;
    classDef detail fill:#1e293b,stroke:#475569,stroke-width:1px,color:#cbd5e1;

    EQ["⚖️ ACTIVO = PASIVO + PATRIMONIO<br/><i>(Ecuación Contable Fundamental)</i>"]:::main

    P1["① REGISTRAR<br/><b>(Entrada de Datos)</b>"]:::step
    P2["② ANALIZAR<br/><b>(Control y Cuadre)</b>"]:::step
    P3["③ EEFF<br/><b>(Salida y Reportes)</b>"]:::step

    EQ --> P1
    EQ --> P2
    EQ --> P3

    subgraph Fase1 ["Fase 1: Registro"]
        P1 --> D1_1["✓ Operaciones económicas<br/><i>(Compras, ventas, cobros, pagos)</i>"]:::detail
        P1 --> D1_2["✓ Plan de cuentas (PCGE)<br/><i>(Elementos 1 al 9)</i>"]:::detail
    end

    subgraph Fase2 ["Fase 2: Análisis"]
        P2 --> D2_1["✓ Que todo esté registrado<br/><i>(Integridad del periodo)</i>"]:::detail
        P2 --> D2_2["✓ Cuentas correctas<br/><i>(Validación de saldos y asientos)</i>"]:::detail
    end

    subgraph Fase3 ["Fase 3: Estados Financieros"]
        P3 --> D3_1["✓ Reporte Financiero<br/><i>(Balance General / EERR / Flujo)</i>"]:::detail
        P3 --> D3_2["✓ Toma de Decisiones<br/><i>(Gerencia, Bancos, SUNAT)</i>"]:::detail
    end
```

---

## 🔍 2. Desglose Conceptual de la Pizarra

### ⚖️ Eje Central: Ecuación Contable Fundamental
$$\text{Activo} = \text{Pasivo} + \text{Patrimonio}$$

* **Activo:** Conjunto de recursos económicos, bienes y derechos controlados por la entidad.
* **Pasivo:** Obligaciones presentes con terceros (bancos, proveedores, tributos).
* **Patrimonio:** Participación residual de los accionistas o dueños una vez deducidos todos los pasivos.
* **Principio rector:** La **Partida Doble** (*no hay deudor sin acreedor*). Cualquier cambio en el Activo debe tener su contrapartida exacta en Pasivo o Patrimonio.

---

### ① Fase 1: REGISTRAR (Captura de Hechos Económicos)
* **Operaciones económicas:** Todo evento comercial o financiero medible en dinero (compras de mercadería, ventas de bienes/servicios, planillas de sueldos, pagos bancarios, etc.).
* **Plan Contable General Empresarial (PCGE):** Estandarización de las cuentas en Perú:
  * *Elementos 1, 2 y 3:* Cuentas del Activo.
  * *Elemento 4:* Cuentas del Pasivo.
  * *Elemento 5:* Cuentas del Patrimonio.
  * *Elemento 6 y 7:* Gastos e Ingresos por naturaleza.
  * *Elemento 8 y 9:* Cierre contable y costos.

---

### ② Fase 2: ANALIZAR (Auditoría Interna y Cuadre)
* **Todo esté registrado:** Garantizar el principio de **integridad** (que no falte ninguna factura de compras, ventas o movimientos de extractos bancarios del periodo).
* **Cuentas correctas:** Verificar que:
  * Los asientos estén correctamente imputados (evitar cargar cuentas equivocadas).
  * Las conciliaciones bancarias cuadren al céntimo.
  * Se elabore el **Balance de Comprobación** (Hoja de Trabajo) verificando la igualdad de sumas y saldos.

---

### ③ Fase 3: EEFF (Estados Financieros / Reporte Final)
* **Reporte Financiero:** Generación de los 4 estados financieros bajo NIIF:
  1. **Estado de Situación Financiera:** Reflejo directo de la fórmula $\text{Activo} = \text{Pasivo} + \text{Patrimonio}$.
  2. **Estado de Resultados:** Ganancias y pérdidas del ejercicio.
  3. **Estado de Flujos de Efectivo:** Entradas y salidas reales de liquidez.
  4. **Estado de Cambios en el Patrimonio Neto:** Variaciones en capital y reservas.
* **Propósito:** Brindar información fidedigna para la toma de decisiones estratégicas, auditorías tributarias ante SUNAT y financiamiento bancario.
