from .errors import CSVFormatError

EXPECTED_COLUMNS = {"nombre", "poblacion", "superficie", "continente"}

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