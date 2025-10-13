from src.datos import cargar_paises
from src.menu import menu_loop

CSV_PATH = 'data/paises.csv'

def main():
    try:
        paises = cargar_paises(CSV_PATH)
    except Exception as e:
        print(f"No se pudo cargar el CSV: {e}")
        return
    menu_loop(paises)

if __name__ == '__main__':
    main()