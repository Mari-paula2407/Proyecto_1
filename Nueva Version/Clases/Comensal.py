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