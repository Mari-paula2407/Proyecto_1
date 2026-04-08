from modelos.plato import Plato
from modelos.menu_dia import MenuDia
from modelos.comensal import Comensal
from servicios.procesador_venta import ProcesadorVenta
from servicios.servicio_pago import ServicioPago
from reportes.generador_reportes import GeneradorReportes

def main():
    # Crear menú vacío
    menu = MenuDia("2026-03-13")

    # Crear servicios (inyectados)
    servicio_pago = ServicioPago()
    procesador = ProcesadorVenta(servicio_pago)
    reporte = GeneradorReportes()

    ventas = []

    # Simulación de uso dinámico (sin datos fijos)
    while True:
        print("\n--- Sistema NutriUTP ---")
        print("1. Agregar plato")
        print("2. Ver menú")
        print("3. Comprar plato")
        print("4. Ver reporte")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del plato: ")
            precio = float(input("Precio base: "))
            veg = input("¿Es vegetariano? (s/n): ").lower() == "s"

            plato = Plato(nombre, precio, veg)
            menu.agregar_plato(plato)

        elif opcion == "2":
            for p in menu.mostrar_menu():
                print(p)

        elif opcion == "3":
            tipo = input("Preferencia (vegetariano/estandar): ")
            plato = menu.seleccionar_opcion(tipo)

            if not plato:
                print("No hay opción disponible")
                continue

            id_est = input("ID estudiante: ")
            tipo_sub = input("Tipo subsidio (alto/medio/bajo/ninguno): ")

            estudiante = Comensal(id_est, tipo_sub)

            venta = procesador.generar_tiquete(estudiante, plato)

            if isinstance(venta, dict):
                ventas.append(venta)
                print("Venta realizada:", venta)
            else:
                print(venta)

        elif opcion == "4":
            print(reporte.generar_resumen(ventas))

        elif opcion == "5":
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()