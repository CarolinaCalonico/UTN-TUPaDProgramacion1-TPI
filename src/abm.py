from typing import Iterable
from .validaciones import (
    validar_no_vacio, validar_entero_positivo, validar_continente
)

def _existe_nombre(paises: Iterable[dict], nombre: str) -> bool:
    n = nombre.casefold().strip()
    return any(p["nombre"].casefold() == n for p in paises)

def agregar_pais_interactivo(paises: list[dict]) -> None:
    """Solicita datos por consola, valida y agrega un nuevo país."""
    print("\n— Alta de país —")
    try:
        nombre = validar_no_vacio(input("Nombre: "), "nombre")
        if _existe_nombre(paises, nombre):
            print("Error: ya existe un país con ese nombre.")
            return
        poblacion = validar_entero_positivo(input("Población (entero): "), "poblacion")
        superficie = validar_entero_positivo(input("Superficie en km² (entero): "), "superficie")
        continente = validar_continente(input("Continente (América/Europa/Asia/África/Oceanía): "))

        paises.append({
            "nombre": nombre.strip(),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        })
        print("OK: país agregado.")
    except ValueError as e:
        print(f"Error: {e}")

def actualizar_pais_interactivo(paises: list[dict]) -> None:
    """Actualiza población y superficie de un país existente (por nombre)."""
    print("\n— Actualizar país —")
    nombre = input("Nombre del país a actualizar: ").strip()
    # buscar
    matches = [p for p in paises if p["nombre"].casefold() == nombre.casefold()]
    if not matches:
        print("Sin resultados: no se encontró un país con ese nombre.")
        return
    p = matches[0]
    try:
        nueva_pob = validar_entero_positivo(input("Nueva población (entero): "), "poblacion")
        nueva_sup = validar_entero_positivo(input("Nueva superficie en km² (entero): "), "superficie")
        p["poblacion"] = nueva_pob
        p["superficie"] = nueva_sup
        print("OK: país actualizado.")
    except ValueError as e:
        print(f"Error: {e}")