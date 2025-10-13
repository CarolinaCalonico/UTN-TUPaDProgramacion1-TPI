from typing import Iterable

def ordenar(paises: Iterable[dict], clave: str, descendente: bool = False) -> list[dict]:
    if clave not in ("nombre", "poblacion", "superficie"):
        raise ValueError("clave debe ser 'nombre', 'poblacion' o 'superficie'")
    return sorted(paises, key=lambda p: p[clave], reverse=descendente)