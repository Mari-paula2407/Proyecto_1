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