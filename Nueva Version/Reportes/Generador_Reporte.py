class GeneradorReportes:
    def generar_resumen(self, ventas):
        total = sum(v["precio_final"] for v in ventas)
        return {
            "total_recaudado": total,
            "cantidad_ventas": len(ventas)
        }