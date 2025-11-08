# filtros.py
# Filtros sobre la colección de países:
# - Por continente (igualdad exacta, insensible a mayús/minús).
# - Por rango numérico (población o superficie), con límites opcionales.

from typing import Iterable

def filtrar_por_continente(paises: Iterable[dict], continente: str) -> list[dict]:
    """
    Devuelve los países cuyo 'continente' coincide exactamente con el provisto
    (comparación insensible a mayúsculas/minúsculas).

    Nota: aquí NO se normalizan tildes; si se ingresa 'america' sin tilde,
    no matcheará 'América'. La consigna actual mantiene las tildes.
    """
    c = continente.lower().strip()
    return [p for p in paises if p["continente"].lower() == c]

def filtrar_por_rango(
    paises: Iterable[dict],
    campo: str,
    minimo: int | None,
    maximo: int | None
) -> list[dict]:
    """
    Filtra por un rango en el 'campo' indicado ('poblacion' o 'superficie').

    - 'minimo' y/o 'maximo' pueden ser None para omitir ese límite.
    - Si 'campo' no es válido, levanta ValueError.
    - Devuelve una nueva lista con los registros dentro del rango.
    """
    if campo not in ("poblacion", "superficie"):
        raise ValueError("campo debe ser 'poblacion' o 'superficie'")

    res: list[dict] = []
    for p in paises:
        v = p[campo]
        # Si hay mínimo y el valor es menor, descarta
        if minimo is not None and v < minimo:
            continue
        # Si hay máximo y el valor es mayor, descarta
        if maximo is not None and v > maximo:
            continue
        res.append(p)
    return res