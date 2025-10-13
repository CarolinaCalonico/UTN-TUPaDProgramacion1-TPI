from typing import Iterable

def buscar_por_nombre(paises: Iterable[dict], termino: str) -> list[dict]:
    t = termino.lower().strip()
    return [p for p in paises if t in p["nombre"].lower()]