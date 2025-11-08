# main.py
# Punto de entrada de la aplicación.
# - Carga el dataset desde CSV.
# - Inicia el bucle de menú para operar sobre la lista en memoria.

from src.datos import cargar_paises
from src.menu import menu_loop

CSV_PATH = 'data/paises.csv'

def main():
    """
    Orquesta la ejecución:
      1) Intenta cargar el CSV (con validación de columnas y tipado).
      2) Si falla, informa el motivo y termina sin romper la app.
      3) Si carga OK, delega el control al menú interactivo.
    """
    try:
        paises = cargar_paises(CSV_PATH)
    except Exception as e:
        # Mensaje claro ante problemas de archivo/formato/tipos.
        print(f"No se pudo cargar el CSV: {e}")
        return

    # Bucle principal de interacción (agregar, actualizar, filtrar, etc.).
    menu_loop(paises)

if __name__ == '__main__':
    main()
