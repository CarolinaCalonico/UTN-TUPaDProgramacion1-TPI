from typing import Iterable

def filtrar_por_continente(paises: Iterable[dict], continente: str) -> list[dict]:
    c = continente.lower().strip()
    return [p for p in paises if p["continente"].lower() == c]

def filtrar_por_rango(paises: Iterable[dict], campo: str,
                      minimo: int | None, maximo: int | None) -> list[dict]:
    if campo not in ("poblacion", "superficie"):
        raise ValueError("campo debe ser 'poblacion' o 'superficie'")
    res: list[dict] = []
    for p in paises:
        v = p[campo]
        if minimo is not None and v < minimo:
            continue
        if maximo is not None and v > maximo:
            continue
        res.append(p)
    return res