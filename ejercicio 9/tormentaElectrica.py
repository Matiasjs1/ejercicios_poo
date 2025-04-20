from tormenta import Tormenta
class TormentaElectrica(Tormenta):
    def __init__(self, nombre, intensidad, velocidad_viento, region):
        super().__init__(nombre, intensidad, velocidad_viento, region)

    def calcular_peligrosidad(self):
        return super().calcular_peligrosidad()*2

#<>