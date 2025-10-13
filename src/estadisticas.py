from collections import Counter
from typing import Iterable

def max_min_poblacion(paises: Iterable[dict]) -> tuple[dict, dict]:
    if not paises:
        raise ValueError("Lista vacía")
    max_p = max(paises, key=lambda p: p["poblacion"])
    min_p = min(paises, key=lambda p: p["poblacion"])
    return max_p, min_p

def promedios(paises: Iterable[dict]) -> tuple[float, float]:
    if not paises:
        raise ValueError("Lista vacía")
    n = len(paises)
    prom_pob = sum(p["poblacion"] for p in paises) / n
    prom_sup = sum(p["superficie"] for p in paises) / n
    return prom_pob, prom_sup

def cantidad_por_continente(paises: Iterable[dict]) -> dict[str, int]:
    c = Counter(p["continente"] for p in paises)
    return dict(c)