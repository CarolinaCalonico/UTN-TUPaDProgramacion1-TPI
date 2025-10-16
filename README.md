# Gestión de Países — TPI Programación 1 (UTN TUP a Distancia)

## Descripción del proyecto
Aplicación de consola en **Python 3** que gestiona un dataset de países desde un **CSV**. Permite:
- **Agregar** un país (con todos los campos obligatorios, sin vacíos).
- **Actualizar** población y superficie de un país existente.
- **Buscar** por nombre (parcial o exacto).
- **Filtrar** por continente y por **rangos** de población/superficie.
- **Ordenar** por nombre, población o superficie (asc/desc).
- **Estadísticas**: mayor/menor población, promedios y cantidad por continente.

> Los cambios realizados (altas/actualizaciones) se **guardan automáticamente** en `data/paises.csv`.

## Datos de la Universidad y la cátedra
- **Universidad:** UTN — TUP a Distancia  
- **Materia:** Programación I  
- **Cuatrimestre/Año:** 1.º C 2025  
- **Trabajo:** Trabajo Práctico Integrador (TPI)

## Integrantes
- **Integrante 1:** Carolina Calonico - 40.094.084 - carolinacalonico@hotmail.com 
- **Integrante 2:** _Nombre Apellido — DNI — Email_

## Docentes
- **Titular / Adjunta/o / Ayudante:** _Completar_

## Estructura del repositorio
```
TPI_Paises/
├─ main.py
├─ README.md
├─ data/
│ └─ paises.csv
└─ src/
├─ __init__.py
├─ datos.py # carga de CSV
├─ validaciones.py # validación de columnas y tipos
├─ errors.py # excepciones propias
├─ busquedas.py # búsquedas por nombre
├─ filtros.py # filtros (continente, rangos)
├─ ordenamiento.py # ordenar por campo (asc/desc)
├─ estadisticas.py # max/min, promedios, conteo por continente
├─ abm.py # altas y actualizaciones
└─ menu.py # interfaz en consola
```

## Instrucciones de ejecución (VS Code)

Requisitos: **Python 3.10+** (probado en 3.13.5).

1. Abrir el proyecto en **VS Code**.
2. Ir a **Terminal → New Terminal**.
3. Asegurarte de que la terminal esté ubicada en la **carpeta raíz** del proyecto (donde está `main.py`).
4. Escribir y ejecutar: 
python main.py
> Si no funciona `python`, probá **en la misma terminal de VS Code**:  
> `python3 main.py`  (Mac/Linux)  **o**  `py -3.10 main.py`  (Windows con Python Launcher).

Al ejecutar, vas a ver el **menú** en consola (búsquedas, filtros, ordenamientos y estadísticas). Salís con la opción **0**.

## Uso de librerías de terceros

No se utilizan librerías de terceros. Solo biblioteca estándar de Python (csv, collections, typing).

## Links

Repositorio GitHub: agregar URL

Video (10–15 min): agregar URL

## Ejemplos de entrada y salida

Se aceptan en estos formatos tanto países como continentes: américa/América/AMÉRICA, respetando los acentos.

1) Agregar país

Entrada:

1
Uruguay
3518550
176215
América

Salida:

OK: país agregado.

2) Actualizar población y superficie

Entrada:

2
Argentina
46000000
2780400

Salida:

OK: país actualizado.

3) Búsqueda por nombre (parcial)

Entrada:

1
arg

Salida:

Argentina        | Pob:  45.376.763 | Sup:   2.780.400 km² | América

4) Filtro por continente

Entrada:

2
Europa

Salida:

Alemania        | Pob: 83.149.300 | Sup:    357.022 km² | Europa
Francia         | Pob: 67.391.582 | Sup:    551.695 km² | Europa
España          | Pob: 47.351.567 | Sup:    505.990 km² | Europa
Italia          | Pob: 59.554.023 | Sup:    301.340 km² | Europa
Rusia           | Pob: 144.104.080 | Sup: 17.098.242 km² | Europa

### 5) Rango de población


**Entrada:**

3
Mínimo (ENTER para ninguno): 100000000
Máximo (ENTER para ninguno): 500000000

**Salida:**

```
Brasil          | Pob: 213.993.437 | Sup:  8.515.767 km² | América
Estados Unidos  | Pob: 331.002.651 | Sup:  9.833.517 km² | América
México          | Pob: 128.932.753 | Sup:  1.964.375 km² | América
Rusia           | Pob: 144.104.080 | Sup: 17.098.242 km² | Europa
Japón           | Pob: 125.800.000 | Sup:    377.975 km² | Asia
Nigeria         | Pob: 206.139.589 | Sup:    923.768 km² | África
Egipto          | Pob: 102.334.404 | Sup:  1.002.450 km² | África
```

6) Rango de superficie

Entrada:

Mínimo (ENTER para ninguno): 3000000
Máximo (ENTER para ninguno): 9000000

Salida:

OK: se encontraron 3 registros.
Brasil          | Pob: 213.993.437 | Sup:  8.515.767 km² | América
India           | Pob: 1.393.409.038 | Sup:  3.287.263 km² | Asia
Australia       | Pob: 25.687.041 | Sup:  7.692.024 km² | Oceanía

7) Ordenamiento por superficie descendente

Entrada:

5
superficie
b

Salida:

Rusia           | Pob: 144.104.080 | Sup: 17.098.242 km² | Europa
Canadá          | Pob: 38.005.238 | Sup:  9.984.670 km² | América
Estados Unidos  | Pob: 331.002.651 | Sup:  9.833.517 km² | América
China           | Pob: 1.411.778.724 | Sup:  9.596.961 km² | Asia
Brasil          | Pob: 213.993.437 | Sup:  8.515.767 km² | América
Australia       | Pob: 25.687.041 | Sup:  7.692.024 km² | Oceanía
India           | Pob: 1.393.409.038 | Sup:  3.287.263 km² | Asia
Argentina       | Pob: 45.376.763 | Sup:  2.780.400 km² | América
Arabia Saudita  | Pob: 34.813.867 | Sup:  2.149.690 km² | Asia
México          | Pob: 128.932.753 | Sup:  1.964.375 km² | América
Sudáfrica       | Pob: 59.308.690 | Sup:  1.221.037 km² | África
Egipto          | Pob: 102.334.404 | Sup:  1.002.450 km² | África
Nigeria         | Pob: 206.139.589 | Sup:    923.768 km² | África
Chile           | Pob: 19.116.209 | Sup:    756.102 km² | América
Francia         | Pob: 67.391.582 | Sup:    551.695 km² | Europa
España          | Pob: 47.351.567 | Sup:    505.990 km² | Europa
Japón           | Pob: 125.800.000 | Sup:    377.975 km² | Asia
Alemania        | Pob: 83.149.300 | Sup:    357.022 km² | Europa
Italia          | Pob: 59.554.023 | Sup:    301.340 km² | Europa
Nueva Zelanda   | Pob:  5.084.300 | Sup:    268.021 km² | Oceanía

## Participación de los integrantes

Integrante 1: diseño de módulos, filtros y ordenamientos; armado de README; grabación de la primera mitad del video.

Integrante 2: estadísticas y validaciones; carga/parseo de CSV; conclusiones y segunda mitad del video.

## Notas

El programa controla errores de formato en el CSV, evita fallos por filtros inválidos y muestra mensajes claros de error/éxito.

Dataset base: data/paises.csv.
