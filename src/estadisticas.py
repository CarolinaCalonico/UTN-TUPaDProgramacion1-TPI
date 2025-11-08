# estadisticas.py
# Cálculos agregados (estadísticas) sobre la colección de países.

from collections import Counter
from typing import Iterable

def max_min_poblacion(paises: Iterable[dict]) -> tuple[dict, dict]:
    """
    Devuelve una tupla (max_p, min_p) con los países de mayor y menor población.

    - Si 'paises' está vacío, levanta ValueError (el llamador decide cómo informar).
    - Usa max/min con key para no recorrer manualmente.
    """
    if not paises:
        raise ValueError("Lista vacía")
    max_p = max(paises, key=lambda p: p["poblacion"])
    min_p = min(paises, key=lambda p: p["poblacion"])
    return max_p, min_p

def promedios(paises: Iterable[dict]) -> tuple[float, float]:
    """
    Calcula promedios de población y superficie.

    Retorna (promedio_poblacion, promedio_superficie) como floats.
    - Si 'paises' está vacío, levanta ValueError.
    - Se usa sum(...) / n (no requiere librerías externas).
    """
    if not paises:
        raise ValueError("Lista vacía")
    n = len(paises)
    prom_pob = sum(p["poblacion"] for p in paises) / n
    prom_sup = sum(p["superficie"] for p in paises) / n
    return prom_pob, prom_sup

def cantidad_por_continente(paises: Iterable[dict]) -> dict[str, int]:
    """
    Cuenta cuántos países hay por continente.

    - Usa collections.Counter para agrupar por p["continente"].
    - Devuelve un dict clásico (ej.: {"América": 5, "Europa": 4, ...}).
    """
    c = Counter(p["continente"] for p in paises)
    return dict(c)