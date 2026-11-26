# Analizador electoral Bolivia 2019

Aplicación para validar resultados por mesa y señalar registros que requieren revisión. No determina fraude ni reemplaza una auditoría.

## Instalación

Requiere Python 3.10 o superior.

    python -m venv .venv

En Windows: \`.venv\Scripts\activate\`
En Linux/macOS: \`source .venv/bin/activate\`

    pip install -r requirements.txt
    streamlit run app.py

## Formato del archivo

Una fila por mesa. Columnas obligatorias:

| Columna | Descripción |
|---|---|
| codigo_mesa | Identificador oficial de mesa/acta |
| departamento | Departamento |
| municipio | Municipio |
| inscritos | Personas inscritas |
| emitidos | Votos emitidos |
| validos | Votos válidos |
| blancos | Votos blancos |
| nulos | Votos nulos |

Columnas opcionales por partido: \`votos_MAS\`, \`votos_CC\`, \`votos_PDC\`, etc. La suma de votos partidarios debe coincidir con válidos cuando estén todas las candidaturas incluidas.

No mezcles resultados preliminares TREP con cómputo oficial sin registrar fuente, versión y hora de corte.

## Reglas

- Códigos de mesa duplicados.
- Datos faltantes, negativos o no enteros.
- Emitidos mayores que inscritos.
- Válidos + blancos + nulos distintos de emitidos.
- Suma de votos por partido distinta de válidos.
- Valores atípicos con z-score modificado basado en MAD (solo con suficientes registros).

Las alertas estadísticas identifican valores inusuales, no irregularidades probadas. Cada caso debe contrastarse con el acta y el contexto.

## Pruebas

    pytest -q

## Fuentes

OEP, Elecciones Generales 2019:
https://web.oep.org.bo/elecciones-generales-2019/

Publicación de resultados nacionales:
https://web.oep.org.bo/wp-content/uploads/2019/11/Separata_Resultados_Nacionales_EG_2019.pdf

Consulta histórica de actas SIMOBOL:
https://computosanteriores.oep.org.bo/simobol_2019_3_Computo/listaMesas.html

El PDF nacional es agregado y no constituye por sí mismo una base tabular completa por mesa. Antes del análisis masivo, normaliza una base de datos por mesa y documenta extracción, URL, fecha, versión y hash SHA-256. No inventes ni completes datos faltantes.

## Interpretación responsable

El programa no puede detectar “todo lo sospechoso”. Solo encuentra patrones definidos en los datos disponibles. No demuestra intención, manipulación o fraude. Presenta sus resultados como alertas verificables.
