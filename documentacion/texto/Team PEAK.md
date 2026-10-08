# Team PEAK

> Versión de texto generada automáticamente a partir de `Team PEAK.docx`.

Análisis Estadístico e Informático de las Elecciones Generales de Bolivia (Caso Edgar Villegas)

Estudiantes:

-Sebastian Matias Alba Ordoñez

-Hugo Santiago Gutierrez Martinez

-Gabriel Santiago Rivero Rico

Universidad: Facultad de tecnología, Universidad Franz Tamayo

Materia: Probabilidad y Estadística

Paralelo: Número 3

1. Organización del Equipo de Desarrollo

1.1. Identificación del Equipo y Estructura Organizativa

Nombre del equipo de desarrollo: Team Peak

Integrantes: Hugo Gutierrez, Matias Alba y Santiago Rivero.

El equipo se organiza de forma colaborativa dividiendo las tareas según las fortalezas de cada integrante. Esta estructura nos permite repartir el trabajo de manera clara, separando la investigación del contexto electoral, recolección del padrón/actas y redacción del proyecto, de la parte de programación, limpieza de bases de datos y cálculo de anomalías probabilísticas.

1.2. Roles Asignados y Responsabilidades

Hugo Gutierrez — Coordinador del Proyecto y Analista de Datos

Coordinación y Tiempos: Control del calendario de entregas y seguimiento del avance de las tareas del grupo.

Investigación del Tema: Recopilación de las actas públicas del Órgano Electoral Plurinacional (OEP), documentación del caso de estudio (metodología de Edgar Villegas, informes del TREP y de la OEA) y redacción de los documentos del proyecto.

Viabilidad y Anexos: Definición del alcance del sistema informático, análisis del impacto del algoritmo de detección de anomalías y armado de la sección de Anexos con evidencia documental.

Matias Alba — Programador de Lógica y Modelos Estadísticos

Modelado Estadístico: Aplicación de las fórmulas de probabilidad, pruebas de correlación, análisis de discrepancias numéricas y modelos de detección de valores atípicos (outliers) en código de Python.

Procesamiento de Datos: Programación del backend del sistema para el filtrado, parseo y comparación automatizada entre el cómputo cargado en la base de datos y la lectura directa/esperada de los votos por mesa.

Control de Archivos: Creación y manejo de la carpeta compartida en GitHub para mantener la versión del código y la carga de conjuntos de datos (datasets) ordenados.

Santiago Rivero — Programador de Pantallas e Interfaz de Usuario

Diseño de Pantalla: Creación del panel visual e interactivo para que el usuario pueda visualizar las actas analizadas, gráficos de distribución de votos por recinto y alertas de actas sospechosas de manera clara.

Unión de Componentes: Conexión de la interfaz visual con el motor de cálculo estadístico desarrollado en Python.

Revisiones y Pruebas: Comprobación de que el sistema procese correctamente archivos CSV/JSON masivos de actas sin errores de ejecución ni retardos en la interfaz.

1.3. Distribución de Tareas por Fases

1.4. Mecanismos de Coordinación y Trabajo Colaborativo

Para trabajar de forma ordenada y al día, el grupo utilizará las siguientes herramientas y métodos:

Manejo de Tareas: Usaremos un tablero de tareas dividido en cuatro columnas (Por Hacer, En Proceso, En Revisión y Terminado) para tener visibilidad continua sobre el estado del análisis y desarrollo informático.

Canales de Comunicación:

WhatsApp: Para avisos rápidos, coordinación de entregables y resolución de dudas puntuales.

Discord: Para sesiones de trabajo remoto, compartir pantalla al momento de programar el script en Python y redactar en conjunto los reportes de anomalías.

Control de Código (GitHub): Matias y Santiago usarán GitHub para el control de versiones del proyecto. Esto permitirá almacenar los scripts de procesamiento de datos, versionar los datasets formateados y evitar la pérdida de avances durante la integración del sistema.


## Tabla 1


| Fase de Trabajo | Tareas Principales | Responsables |

| --- | --- | --- |

| Fase 1: Investigación y Modelado | • Recopilación y estructuración del conjunto de datos de actas electorales (TREP / Cómputo Oficial).   • Definición de variables estadísticas (votos nulos, blancos, variaciones drásticas porcentuales, patrones de firmas y patrones de corte de cómputo).   • Elección de las fórmulas probabilísticas para la detección de anomalías. | Hugo Gutierrez   Matias Alba |

| Fase 2: Desarrollo y Programación | • Programación de los algoritmos de detección de discrepancias e inconsistencias en Python.   • Diseño e implementación del panel de control web para la visualización gráfica de resultados por departamento y recinto electoral.   • Vinculación del módulo visual con los cálculos estadísticos en tiempo real. | Matias Alba   Santiago Rivero |

| Fase 3: Documentación y Revisiones | • Pruebas cruzadas para verificar el porcentaje de acierto de las anomalías detectadas en las actas auditadas.   • Redacción del informe final, interpretación probabilística de los hallazgos y armado de anexos. | Todo el equipo (Liderado por Hugo G.) |