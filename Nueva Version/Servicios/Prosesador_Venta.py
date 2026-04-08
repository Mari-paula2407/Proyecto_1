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
            "precio_final": precio_final
        }

    def validar_pago(self, monto):
        return self.servicio_pago.validar_pago(monto)