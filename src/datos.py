from csv import DictReader, DictWriter
from .validaciones import validar_columnas, to_int

def cargar_paises(path_csv: str) -> list[dict]:
    """Carga CSV -> lista de dicts tipados."""
    try:
        with open(path_csv, 'r', encoding='utf-8') as f:
            reader = DictReader(f)
            validar_columnas(reader.fieldnames)
            paises: list[dict] = []
            for i, row in enumerate(reader, start=2):
                paises.append({
                    "nombre": row["nombre"].strip(),
                    "poblacion": to_int(row["poblacion"], "poblacion", i),
                    "superficie": to_int(row["superficie"], "superficie", i),
                    "continente": row["continente"].strip()
                })
            return paises
    except FileNotFoundError as e:
        raise FileNotFoundError(f"No se encontró el archivo CSV en {path_csv}") from e

def guardar_paises(path_csv: str, paises: list[dict]) -> None:
    """Persiste la lista de países nuevamente en el CSV."""
    with open(path_csv, 'w', newline='', encoding='utf-8') as f:
        writer = DictWriter(f, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        writer.writeheader()
        for p in paises:
            writer.writerow({
                "nombre": p["nombre"],
                "poblacion": p["poblacion"],
                "superficie": p["superficie"],
                "continente": p["continente"]
            })