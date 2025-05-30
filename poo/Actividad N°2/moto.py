from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, matricula, hora_entrada):
        super().__init__(matricula, hora_entrada)
        self.tipo = "Moto"

    