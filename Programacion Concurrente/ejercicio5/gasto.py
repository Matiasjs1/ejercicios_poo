from operacion import Operacion
class Gasto(Operacion):
    def __init__(self):
        pass
    def calcular_total(self):
        total = 0
        with open("gastos.txt", "r") as archivo:
            for linea in archivo:
                total += float(linea.strip())
        return total
    def agregar_gasto(self,valorGasto):
        if valorGasto <= 0:
            raise ValueError("El valor fue menor o igual a 0")
        with open("gastos.txt", "a") as archivo:
            archivo.write(f"{valorGasto}")
        