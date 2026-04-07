# ==============================
# MODELOS
# ==============================

class Plato:
    def __init__(self, nombre, precio_base, es_vegetariano):
        self.nombre = nombre
        self._precio_base = precio_base
        self.es_vegetariano = es_vegetariano

    def precio(self):
        return self._precio_base

    def descripcion_detallada(self):
        tipo = "Vegetariano" if self.es_vegetariano else "Estándar"
        return f"{self.nombre} - {tipo} - ${self._precio_base}"


class MenuDia:
    def __init__(self, fecha):
        self.fecha = fecha
        self._opciones = []

    def agregar_plato(self, plato):
        self._opciones.append(plato)

    def seleccionar_opcion(self, tipo_preferencia):
        return self._aislar_seleccion(tipo_preferencia)

    def _aislar_seleccion(self, tipo_preferencia):
        for plato in self._opciones:
            if tipo_preferencia == "vegetariano" and plato.es_vegetariano:
                return plato
            elif tipo_preferencia == "estandar" and not plato.es_vegetariano:
                return plato
        return None

    def mostrar_menu(self):
        return [p.descripcion_detallada() for p in self._opciones]


class Comensal:
    def __init__(self, id_estudiante, tipo_subsidio):
        self.id_estudiante = id_estudiante
        self.tipo_subsidio = tipo_subsidio

    def calcular_descuento(self, valor_plato):
        if self.tipo_subsidio == "alto":
            return valor_plato * 0.5
        elif self.tipo_subsidio == "medio":
            return valor_plato * 0.7
        elif self.tipo_subsidio == "bajo":
            return valor_plato * 0.9
        else:
            return valor_plato


# ==============================
# SERVICIOS
# ==============================

class ServicioPago:
    def validar_pago(self, monto):
        print(f"Validando pago por ${monto}...")
        return True


class ProcesadorVenta:
    def __init__(self, servicio_pago):
        self.servicio_pago = servicio_pago

    def generar_tiquete(self, estudiante, plato):
        precio_base = plato.precio()
        precio_final = estudiante.calcular_descuento(precio_base)

        if not self.validar_pago(precio_final):
            return "Pago rechazado"

        return {
            "estudiante": estudiante.id_estudiante,
            "plato": plato.nombre,
            "precio_base": precio_base,
            "precio_final": precio_final
        }

    def validar_pago(self, monto):
        return self.servicio_pago.validar_pago(monto)


# ==============================
# REPORTES
# ==============================

class GeneradorReportes:
    def generar_resumen(self, ventas):
        total = sum(v["precio_final"] for v in ventas)
        return {
            "total_recaudado": total,
            "cantidad_ventas": len(ventas)
        }


# ==============================
# MAIN
# ==============================

def main():
    # Crear menú
    menu = MenuDia("2026-03-13")

    plato1 = Plato("Pollo con arroz", 10000, False)
    plato2 = Plato("Ensalada vegetariana", 8000, True)

    menu.agregar_plato(plato1)
    menu.agregar_plato(plato2)

    print("📋 Menú del día:")
    for p in menu.mostrar_menu():
        print(p)

    # Crear estudiante
    estudiante = Comensal("123", "alto")

    # Seleccionar plato
    plato = menu.seleccionar_opcion("vegetariano")

    if not plato:
        print("No hay opción disponible")
        return

    # Procesar venta
    servicio_pago = ServicioPago()
    procesador = ProcesadorVenta(servicio_pago)

    venta = procesador.generar_tiquete(estudiante, plato)

    print("\n🧾 Tiquete:")
    print(venta)

    # Reporte
    reporte = GeneradorReportes()
    resumen = reporte.generar_resumen([venta])

    print("\n📊 Reporte:")
    print(resumen)


if __name__ == "__main__":
    main()