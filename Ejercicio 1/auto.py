from vehiculo import Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, cantidad_puertas):
        super().__init__(marca, modelo, anio)
        self.cantidad_puertas = cantidad_puertas