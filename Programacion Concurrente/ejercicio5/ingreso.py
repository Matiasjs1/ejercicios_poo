from operacion import Operacion
class Ingreso(Operacion):
    def __init__(self):
        pass

    def calcular_total(self):
        total = 0
        with open("ingresos.txt", "r") as archivo:
            for linea in archivo:
                total += float(linea.strip())
        return total
    
    def agregar_ingreso(self,valorIngreso):
        if valorIngreso <= 0:
            raise ValueError("El valor fue menor o igual a 0")
        with open("ingresos.txt", "a") as archivo:
            archivo.write(f"{valorIngreso}")