from operacion import Operacion
class Gasto(Operacion):
    def __init__ (self, archivo):
        super().__init__(archivo)

    def calcular_total(self):
        print("Se intentara calcular el total de gastos")
        return super().calcular_total()
