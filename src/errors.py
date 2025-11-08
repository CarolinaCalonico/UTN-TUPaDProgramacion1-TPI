# errors.py
# Módulo de excepciones propias del proyecto.
# La idea es concentrar aquí los errores “de dominio” para poder
# importarlos desde datos.py / validaciones.py y mostrar mensajes
# coherentes en toda la app.

class CSVFormatError(Exception):
    """
    Se lanza cuando el archivo CSV no cumple con el formato esperado.

    Casos típicos:
      - Encabezados distintos a los esperados (nombre, poblacion, superficie, continente).
      - Campos numéricos no convertibles (poblacion/superficie).
      - Valores vacíos donde no corresponde durante la carga.
    """
    pass