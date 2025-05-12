from vehiculo import Vehiculo
class Camion(Vehiculo):
    
    def __init__(self, matricula, hora_entrada):
        super().__init__(matricula, hora_entrada)
        self.tipo = "Camión"
        self.tarifa_base = 10 * 1.5
        self.datos = self.matricula, self.hora_entrada, self.tipo

    
    def calcular_tarifa(self):
        hora = self.hora_salida - self.hora_entrada 
        tarifa = self.tarifa_base * hora
        self.tarifa_final = tarifa
