from tormenta import Tormenta
class TormentaElectrica(Tormenta):
    def __init___(self, nombre, intensidad, velocidadViento, region):
        super().__init__(nombre, intensidad, velocidadViento, region)

    def calcularValorPeligrosidad(self):
        total = (self.velocidadViento / 10) + self.intensidad + 10
        return total

    def mostrarInfo(self):
        print("Tormenta Electrica")
        super().mostrarInfo()