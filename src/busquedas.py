# busquedas.py
# Búsquedas sobre la colección de países.

from typing import Iterable

def buscar_por_nombre(paises: Iterable[dict], termino: str) -> list[dict]:
    """
    Devuelve una lista con los países cuyo nombre contiene 'termino'
    (coincidencia parcial, insensible a mayúsculas/minúsculas).

    Parámetros:
      - paises: iterable de dicts con la forma
            {"nombre": str, "poblacion": int, "superficie": int, "continente": str}
      - termino: texto ingresado por la persona usuaria.

    Detalles:
      - .strip() quita espacios al inicio/fin del término buscado.
      - .lower() (o .casefold() si se quisiera más robustez con Unicode)
        asegura comparación sin diferenciar mayúsculas/minúsculas.
      - Se usa list comprehension para construir la lista resultado.
    """
    t = termino.lower().strip()
    return [p for p in paises if t in p["nombre"].lower()]