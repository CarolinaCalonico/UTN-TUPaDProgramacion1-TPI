from .errors import CSVFormatError

EXPECTED_COLUMNS = {"nombre", "poblacion", "superficie", "continente"}
CONTINENTES_VALIDOS = {"américa", "europa", "asia", "áfrica", "oceanía"}

def validar_columnas(fieldnames: list[str] | None) -> None:
    if set(fieldnames or []) != EXPECTED_COLUMNS:
        raise CSVFormatError(
            f"Columnas esperadas {EXPECTED_COLUMNS} y se encontraron {fieldnames}"
        )

def to_int(valor: str, campo: str, fila: int) -> int:
    try:
        return int(valor)
    except Exception as e:
        raise CSVFormatError(f"Fila {fila}: campo '{campo}' inválido -> {valor!r}") from e

# === Validaciones para altas/actualizaciones ===
def validar_no_vacio(texto: str, nombre_campo: str) -> str:
    t = (texto or "").strip()
    if not t:
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
    return t

def validar_entero_positivo(valor: str, nombre_campo: str) -> int:
    v = int(valor)
    if v <= 0:
        raise ValueError(f"El campo '{nombre_campo}' debe ser un entero positivo.")
    return v

def validar_continente(valor: str) -> str:
    v = validar_no_vacio(valor, "continente").lower()
    if v not in CONTINENTES_VALIDOS:
        raise ValueError("Continente inválido. Opciones: América, Europa, Asia, África, Oceanía.")
    # conservar capitalización bonita
    mapping = {
        "américa": "América", "europa": "Europa", "asia": "Asia",
        "áfrica": "África", "oceanía": "Oceanía"
    }
    return mapping[v]