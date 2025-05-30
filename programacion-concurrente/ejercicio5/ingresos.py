from operacion import Operacion
class Ingreso(Operacion):
    def __init__ (self, archivo):
        super().__init__(archivo)

    def calcular_total(self):
        print("Se intentara calcular el total de ingresos")
        return super().calcular_total()
