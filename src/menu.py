from .busquedas import buscar_por_nombre
from .filtros import filtrar_por_continente, filtrar_por_rango
from .ordenamiento import ordenar
from .estadisticas import max_min_poblacion, promedios, cantidad_por_continente

CONTINENTES_VALIDOS = {"américa", "europa", "asia", "áfrica", "oceanía"}

def mostrar_pais(p: dict) -> str:
    return (
        f"{p['nombre']:<15} | Pob: {p['poblacion']:>10,} | "
        f"Sup: {p['superficie']:>10,} km² | {p['continente']}"
    ).replace(',', '.')

def _imprimir_lista(res):
    print("\n".join(mostrar_pais(p) for p in res) or "Sin resultados.")

def menu_loop(paises: list[dict]) -> None:
    while True:
        print("\n=== Gestión de Países ===")
        print("1) Buscar por nombre")
        print("2) Filtrar por continente")
        print("3) Filtrar por rango de población")
        print("4) Filtrar por rango de superficie")
        print("5) Ordenar (nombre/población/superficie)")
        print("6) Estadísticas")
        print("0) Salir")
        op = input("Elegí una opción: ").strip()

        try:
            if op == '1':
                t = input("Nombre o parte: ")
                _imprimir_lista(buscar_por_nombre(paises, t))

            elif op == '2':
                c = input("Continente exacto (América/Europa/Asia/África/Oceanía): ").strip().lower()
                if c not in CONTINENTES_VALIDOS:
                    print("Error: continente inválido. Opciones: América, Europa, Asia, África, Oceanía.")
                else:
                    _imprimir_lista(filtrar_por_continente(paises, c))

            elif op == '3':
                mn = input("Mínimo (ENTER para ninguno): ").strip()
                mx = input("Máximo (ENTER para ninguno): ").strip()
                minimo = int(mn) if mn else None
                maximo = int(mx) if mx else None
                if (minimo is not None and maximo is not None) and minimo > maximo:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    _imprimir_lista(filtrar_por_rango(paises, "poblacion", minimo, maximo))

            elif op == '4':
                mn = input("Mínimo (ENTER para ninguno): ").strip()
                mx = input("Máximo (ENTER para ninguno): ").strip()
                minimo = int(mn) if mn else None
                maximo = int(mx) if mx else None
                if (minimo is not None and maximo is not None) and minimo > maximo:
                    print("Error: el mínimo no puede ser mayor que el máximo.")
                else:
                    _imprimir_lista(filtrar_por_rango(paises, "superficie", minimo, maximo))

            elif op == '5':
                clave = input("Clave (nombre/poblacion/superficie): ").strip().lower()
                desc = input("¿Descendente? (s/n): ").strip().lower() == 's'
                try:
                    _imprimir_lista(ordenar(paises, clave, desc))
                except ValueError as e:
                    print(f"Error: {e}. Claves válidas: nombre, poblacion, superficie.")

            elif op == '6':
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
                print("¡Gracias! Hasta luego.")
                return

            else:
                print("Opción inválida.")
        except ValueError:
            print("Error: se esperaba un número entero.")
        except Exception as e:
            print(f"Error inesperado: {e}")