# ordenamiento.py
# Utilidad de ordenamiento para la colección de países.

from typing import Iterable

def ordenar(paises: Iterable[dict], clave: str, descendente: bool = False) -> list[dict]:
    """
    Devuelve una nueva lista ordenada por la 'clave' indicada.

    Parámetros:
      - paises: iterable de dicts con claves: nombre, poblacion, superficie.
      - clave:  "nombre" | "poblacion" | "superficie"
      - descendente: False => ascendente (default) / True => descendente.

    Detalles:
      - Valida que la clave sea una de las permitidas.
      - Usa sorted(...) con key=lambda p: p[clave] y reverse=descendente.
      - No modifica la lista original (retorna una copia ordenada).
    """
    if clave not in ("nombre", "poblacion", "superficie"):
        raise ValueError("clave debe ser 'nombre', 'poblacion' o 'superficie'")
    return sorted(paises, key=lambda p: p[clave], reverse=descendente)
