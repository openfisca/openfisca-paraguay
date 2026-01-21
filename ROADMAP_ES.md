# Hoja de Ruta de Verificación: Legislación (Enfoque)

Este documento detalla la estrategia para garantizar que el modelo OpenFisca Paraguay refleje fielmente la legislación.
Nos centramos aquí exclusivamente en la validez normativa (Parámetros y Variables).

---

## 🎯 Objetivo
**Lograr un Modelo "Legalmente Exacto".**
Cada parámetro debe tener una fuente. Cada fórmula debe corresponder a la ley.

---

## 📋 Plan de Acción

### Fase 1: Auditoría Estática
*Acción: Revisar y validar lo existente.*

1. **Parámetros (YAML)**
   - Verificar valores e historia en `parameters/`.
   - **Obligatorio**: Cada archivo YAML debe incluir un metadato `reference` estructurado por fecha para cada cambio de valor.
     ```yaml
     metadata:
       reference:
         2024-01-01: # Fecha de vigencia
           title: "Decreto N°..." # Título de la ley/decreto
           href: "https://..." # Enlace al Decreto/Ley
     ```
   - *Objetivos Prioritarios*: Salarios Mínimos, Cotizaciones IPS, Escalas IRP/IRE.

2. **Variables (Python)**
   - Verificar la lógica de las variables en `variables/`.
   - **Historia Legislativa**: Si una fórmula cambió en el tiempo, citar la ley correspondiente a la modificación en el docstring o código.
   - Asegurar que las exenciones y deducciones estén correctamente codificadas.

### Fase 2: Validación Dinámica (Pruebas)
*Acción: Demostrar que los cálculos son correctos.*

1. **Casos Tipo (Perfiles)**
   - Definir 3-5 perfiles "específicos" (ej: Trabajador Salario Mínimo, Familia Tekoporã, Independiente).
   - Simular estos perfiles manualmente (Excel/Papel) para obtener resultados de referencia.

2. **Pruebas de Integración**
   - Implementar estos perfiles en `tests/test_case_types.py`.
   - Verificar que `Resultado OpenFisca == Resultado Excel` (coincidencia exacta / < 1 PYG).

---

## ⚙️ Modo de Acción y Buenas Prácticas

Para colaborar eficazmente entre Negocio (Ernesto) y Tecnología (Benjello), este es el flujo de trabajo recomendado:

### 1. La Regla de Oro: "Una Tarea = Una Rama"
Nunca modificar todo el código a la vez. Trabajar tema por tema.
*Ejemplo: No corregir el Salario Mínimo y el Impuesto a la Renta en el mismo Pull Request.*

### 2. Flujo de Corrección (El Ciclo)
1. **Detección**: Identificar un error en un parámetro o fórmula.
2. **Rama (Branch)**: Crear una rama explícita.
   - *Bien*: `fix/salario-minimo-2023`, `chore/fuente-ips`
   - *Mal*: `ernesto-test`, `correccion`
3. **Corrección y Prueba**:
   - Modificar el valor.
   - **Añadir la fuente**:
     - *Parámetros (YAML)*: Estructura `metadata` / `reference` / `date`.
     - *Variables (Python)*: Comentario o Docstring citando el artículo de la ley.
4. **Pull Request (PR)**: Abrir la PR en GitHub.
   - *Título*: Explícito (ej: "Corrección histórico salario mínimo 2020-2024").
   - *Descripción*: "Basado en el Decreto N°1234 (enlace)".
5. **Revisión (Review)**:
   - **Benjello** revisa: Sintaxis YAML/Python, Indentación, Tests que fallan.
   - **Ernesto** revisa: Conformidad con la ley.
6. **Merge**: Una vez validado por la otra parte, fusionar.

### 3. Gestión de Dudas
Si una ley es ambigua o difícil de codificar:
- No bloquearse.
- Crear un **Issue** en GitHub con la etiqueta `question` o `legislation-check`.
- Copiar allí el texto ambiguo de la ley para discutirlo.
