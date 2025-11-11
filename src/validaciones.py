# validaciones.py
# Reglas de validación y utilidades de tipado/cabeceras para el proyecto.
# - Encabezados del CSV (estructura esperada).
# - Conversión segura a int con mensajes claros (incluye número de fila).
# - Validaciones de entrada para altas/actualizaciones.
# - Normalización/control de continentes (con tildes, case-insensitive).

from .errors import CSVFormatError

# Conjunto exacto de columnas esperadas en el CSV
EXPECTED_COLUMNS = {"nombre", "poblacion", "superficie", "continente"}

# Conjunto de continentes válidos (normalizados a minúsculas con tilde).
# Nota: por decisión del TPI NO se quitan tildes; 'america' (sin tilde) no matchea.
CONTINENTES_VALIDOS = {"américa", "europa", "asia", "áfrica", "oceanía"}

def validar_columnas(fieldnames: list[str] | None) -> None:
    """
    Verifica que los encabezados del CSV coincidan exactamente con EXPECTED_COLUMNS.
    Si no coinciden, levanta CSVFormatError con el detalle de lo encontrado.
    """
    if set(fieldnames or []) != EXPECTED_COLUMNS:
        raise CSVFormatError(
            f"Columnas esperadas {EXPECTED_COLUMNS} y se encontraron {fieldnames}"
        )

def to_int(valor: str, campo: str, fila: int) -> int:
    """
    Convierte 'valor' a int. Si falla, levanta CSVFormatError con el número de fila.
    Útil durante la carga del CSV para diagnosticar registros problemáticos.
    """
    try:
        return int(valor)
    except Exception as e:
        raise CSVFormatError(f"Fila {fila}: campo '{campo}' inválido -> {valor!r}") from e

# === Validaciones para altas/actualizaciones ===

def validar_no_vacio(texto: str, nombre_campo: str) -> str:
    """
    Rechaza strings vacíos/espacios. Devuelve el texto limpio con .strip().
    """
    t = (texto or "").strip()
    if not t:
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
    return t

def validar_entero_positivo(valor: str, nombre_campo: str) -> int:
    t = (valor or "").strip()
    if not t:
        # ENTER / vacío
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
    if not t.isdecimal():
        # letras, símbolos, espacios, signos, etc.
        raise ValueError(f"El campo '{nombre_campo}' debe ser un entero.")
    v = int(t)
    if v <= 0:
        raise ValueError(f"El campo '{nombre_campo}' debe ser un entero positivo.")
    return v

def validar_continente(valor: str) -> str:
    """
    Valida el continente contra CONTINENTES_VALIDOS (case-insensitive, con tildes).
    Devuelve el nombre capitalizado “bonito” para salida uniforme.

    Ej.: 'europa' -> 'Europa' ; 'ÁFRICA' -> 'África'
    """
    v = validar_no_vacio(valor, "continente").lower()
    if v not in CONTINENTES_VALIDOS:
        raise ValueError("Continente inválido. Opciones: América, Europa, Asia, África, Oceanía.")
    # conservar capitalización bonita para las salidas
    mapping = {
        "américa": "América", "europa": "Europa", "asia": "Asia",
        "áfrica": "África", "oceanía": "Oceanía"
    }
    return mapping[v]