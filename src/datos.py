# datos.py
# Capa de acceso a datos: carga y guardado del CSV de países.

from csv import DictReader, DictWriter
from .validaciones import validar_columnas, to_int

def cargar_paises(path_csv: str) -> list[dict]:
    """
    Carga el archivo CSV y devuelve una lista de diccionarios tipados.

    - Abre el CSV con UTF-8.
    - Usa csv.DictReader para mapear cada fila a un dict por encabezado.
    - Valida que los encabezados sean exactamente los esperados.
    - Convierte 'poblacion' y 'superficie' a int con manejo de errores,
      informando el número de línea en caso de problema.
    """
    try:
        with open(path_csv, 'r', encoding='utf-8') as f:
            reader = DictReader(f)

            # Verificación de columnas antes de procesar filas
            validar_columnas(reader.fieldnames)

            paises: list[dict] = []
            # i arranca en 2 porque la línea 1 es el header del CSV
            for i, row in enumerate(reader, start=2):
                paises.append({
                    "nombre": row["nombre"].strip(),                 # normalizamos espacios
                    "poblacion": to_int(row["poblacion"], "poblacion", i),
                    "superficie": to_int(row["superficie"], "superficie", i),
                    "continente": row["continente"].strip()
                })
            return paises

    # Si el archivo no existe, propagamos una excepción con mensaje claro
    except FileNotFoundError as e:
        raise FileNotFoundError(f"No se encontró el archivo CSV en {path_csv}") from e


def guardar_paises(path_csv: str, paises: list[dict]) -> None:
    """
    Persiste la lista en el CSV (sobrescribe el archivo).

    - Escribe encabezados en el orden canónico.
    - Vuelca cada país tal como está en memoria.
    - newline='' evita líneas en blanco extra en Windows.
    """
    with open(path_csv, 'w', newline='', encoding='utf-8') as f:
        writer = DictWriter(
            f,
            fieldnames=["nombre", "poblacion", "superficie", "continente"]
        )
        writer.writeheader()
        for p in paises:
            writer.writerow({
                "nombre": p["nombre"],
                "poblacion": p["poblacion"],
                "superficie": p["superficie"],
                "continente": p["continente"]
            })