from vehiculo import Vehiculo
class Automovil(Vehiculo):
    def __init__(self, matricula, hora_entrada):
        super().__init__(matricula, hora_entrada)
        self.tipo = "Automovil"
        self.tarifa_base = 10
        self.datos = self.matricula, self.hora_entrada, self.tipo
        


    def calcular_tarifa(self):
        hora = self.hora_salida - self.hora_entrada
        tarifa = hora * self.tarifa_base
        self.tarifa_final = tarifa



