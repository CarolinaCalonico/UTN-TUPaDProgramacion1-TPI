# abm.py
# Módulo de Altas/Bajas/Modificaciones (ABM) para la lista de países.
# - Alta: solicita datos, valida y agrega un nuevo país.
# - Actualización: modifica población y superficie de un país existente.
# Las validaciones se delegan en validaciones.py para mantener coherencia.

from typing import Iterable
from .validaciones import (
    validar_no_vacio, validar_entero_positivo, validar_continente
)

def _existe_nombre(paises: Iterable[dict], nombre: str) -> bool:
    """
    Devuelve True si 'nombre' ya existe en la colección 'paises'.

    Normalizamos comparaciones con .casefold() (mejor que lower() para Unicode)
    y .strip() para ignorar espacios extra.
    """
    n = nombre.casefold().strip()
    return any(p["nombre"].casefold() == n for p in paises)

def agregar_pais_interactivo(paises: list[dict]) -> None:
    """
    Solicita datos por consola, valida y agrega un nuevo país a 'paises'.

    Flujo:
      1) Pide nombre y valida no vacío.
      2) Chequea duplicado por nombre (insensible a mayús/minús).
      3) Pide población y superficie como enteros positivos.
      4) Pide continente válido (América/Europa/Asia/África/Oceanía).
      5) Agrega el diccionario a la lista.
    Ante un ValueError de validación, informa y no agrega.
    """
    print("\n— Alta de país —")
    try:
        # Nombre obligatorio (no vacío) y sin espacios de más.
        nombre = validar_no_vacio(input("Nombre: "), "nombre")

        # Evitar duplicados por nombre (normalizado).
        if _existe_nombre(paises, nombre):
            print("Error: ya existe un país con ese nombre.")
            return

        # Campos numéricos: enteros y positivos.
        poblacion = validar_entero_positivo(input("Población (entero): "), "poblacion")
        superficie = validar_entero_positivo(input("Superficie en km² (entero): "), "superficie")

        # Campo categórico: debe pertenecer al conjunto permitido.
        continente = validar_continente(input("Continente (América/Europa/Asia/África/Oceanía): "))

        # Estructura canónica del registro.
        paises.append({
            "nombre": nombre.strip(),
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        })
        print("OK: país agregado.")
    except ValueError as e:
        # Cualquier validación que falle lanza ValueError con un mensaje claro.
        print(f"Error: {e}")

def actualizar_pais_interactivo(paises: list[dict]) -> None:
    """
    Actualiza población y superficie de un país existente (búsqueda por nombre).

    Flujo:
      1) Pide el nombre, busca coincidencia exacta insensible a mayús/minús.
      2) Si no existe, informa y termina.
      3) Valida nuevos valores de población/superficie (enteros positivos).
      4) Sobrescribe los campos en el dict seleccionado.
    """
    print("\n— Actualizar país —")
    nombre = input("Nombre del país a actualizar: ").strip()

    # Búsqueda simple por igualdad normalizada (sin crear estructuras auxiliares).
    matches = [p for p in paises if p["nombre"].casefold() == nombre.casefold()]
    if not matches:
        print("Sin resultados: no se encontró un país con ese nombre.")
        return

    p = matches[0]
    try:
        # Nuevos valores validados.
        nueva_pob = validar_entero_positivo(input("Nueva población (entero): "), "poblacion")
        nueva_sup = validar_entero_positivo(input("Nueva superficie en km² (entero): "), "superficie")

        # Actualización in-place sobre la misma referencia del dict.
        p["poblacion"] = nueva_pob
        p["superficie"] = nueva_sup
        print("OK: país actualizado.")
    except ValueError as e:
        print(f"Error: {e}")