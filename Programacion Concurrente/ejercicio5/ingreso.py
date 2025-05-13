from operacion import Operacion
class Ingreso(Operacion):
    def __init__(self):
        self.archivo_ingresos = "ingresos.txt"

    def calcular_total(self):
        total = 0
        with open(Ingreso.archivo_ingresos, "r") as archivo:
            for linea in archivo:
                total += float(linea.strip())
        return total
    
    def agregar_ingreso(self,valorIngreso):
        if valorIngreso <= 0:
            raise ValueError("El valor fue menor o igual a 0")
        with open(self.archivo_ingresos, "w") as archivo:
            archivo.write(valorIngreso)