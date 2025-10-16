from .busquedas import buscar_por_nombre
from .filtros import filtrar_por_continente, filtrar_por_rango
from .ordenamiento import ordenar
from .estadisticas import max_min_poblacion, promedios, cantidad_por_continente
from .abm import agregar_pais_interactivo, actualizar_pais_interactivo
from .datos import guardar_paises
from .validaciones import CONTINENTES_VALIDOS

CSV_PATH = 'data/paises.csv'  # para persistir al guardar

def mostrar_pais(p: dict) -> str:
    return (
        f"{p['nombre']:<15} | Pob: {p['poblacion']:>10,} | "
        f"Sup: {p['superficie']:>10,} km² | {p['continente']}"
    ).replace(',', '.')

def _imprimir_lista(res):
    if not res:
        print("Sin resultados.")
    else:
        print(f"OK: se encontraron {len(res)} registros.")
        print("\n".join(mostrar_pais(p) for p in res))

def _elegir_sentido() -> bool:
    """
    Pide el sentido de ordenamiento y valida:
    - a -> ascendente  (return False)
    - b -> descendente (return True)
    Repite hasta que el usuario ingrese 'a' o 'b'.
    """
    while True:
        op = input("Elegir orden: a) ascendente  b) descendente: ").strip().lower()
        if op in ("a", "b"):
            return op == "b"
        print("Error: debe seleccionar 'a' o 'b'.")

def menu_loop(paises: list[dict]) -> None:
    while True:
        print("\n=== Gestión de Países ===")
        print("1) Agregar país")
        print("2) Actualizar población y superficie")
        print("3) Buscar por nombre")
        print("4) Filtrar por continente")
        print("5) Filtrar por rango de población")
        print("6) Filtrar por rango de superficie")
        print("7) Ordenar (nombre/población/superficie)")
        print("8) Estadísticas")
        print("0) Guardar y salir")
        op = input("Elegí una opción: ").strip()

        try:
            if op == '1':
                agregar_pais_interactivo(paises)
                guardar_paises(CSV_PATH, paises)

            elif op == '2':
                actualizar_pais_interactivo(paises)
                guardar_paises(CSV_PATH, paises)

            elif op == '3':
                t = input("Nombre o parte: ")
                _imprimir_lista(buscar_por_nombre(paises, t))

            elif op == '4':
                c = input("Continente exacto (América/Europa/Asia/África/Oceanía): ").strip().lower()
                if c not in CONTINENTES_VALIDOS:
                    print("Error: continente inválido. Opciones: América, Europa, Asia, África, Oceanía.")
                else:
                    _imprimir_lista(filtrar_por_continente(paises, c))

            elif op == '5':
                mn = input("Mínimo (ENTER para ninguno): ").strip()
                mx = input("Máximo (ENTER para ninguno): ").strip()
                minimo = int(mn) if mn else None
                maximo = int(mx) if mx else None
                if (minimo is not None and maximo is not None) and minimo > maximo:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    _imprimir_lista(filtrar_por_rango(paises, "poblacion", minimo, maximo))

            elif op == '6':
                mn = input("Mínimo (ENTER para ninguno): ").strip()
                mx = input("Máximo (ENTER para ninguno): ").strip()
                minimo = int(mn) if mn else None
                maximo = int(mx) if mx else None
                if (minimo is not None and maximo is not None) and minimo > maximo:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    _imprimir_lista(filtrar_por_rango(paises, "superficie", minimo, maximo))

            elif op == '7':
                clave = input("Clave (nombre/poblacion/superficie): ").strip().lower()
                if clave not in ("nombre", "poblacion", "superficie"):
                    print("Error: clave inválida. Claves válidas: nombre, poblacion, superficie.")
                else:
                    descendente = _elegir_sentido()  # a/b con validación
                    _imprimir_lista(ordenar(paises, clave, descendente))

            elif op == '8':
                mx, mn = max_min_poblacion(paises)
                pp, ps = promedios(paises)
                cc = cantidad_por_continente(paises)
                print("\n— Estadísticas —")
                print("Mayor población:", mostrar_pais(mx))
                print("Menor población:", mostrar_pais(mn))
                print(f"Promedio población: {pp:,.2f}".replace(',', '.'))
                print(f"Promedio superficie: {ps:,.2f} km²".replace(',', '.'))
                print("Países por continente:")
                for k, v in cc.items():
                    print(f"  {k}: {v}")

            elif op == '0':
                guardar_paises(CSV_PATH, paises)
                print("Cambios guardados. ¡Hasta luego!")
                return

            else:
                print("Opción inválida.")
        except ValueError:
            print("Error: se esperaba un número entero.")
        except Exception as e:
            print(f"Error inesperado: {e}")