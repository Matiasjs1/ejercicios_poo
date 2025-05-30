class Operacion():
    def __init__(self, archivo):
        self.archivo = archivo

    def calcular_total(self):
        valorTotal = 0
        with open(self.archivo, 'r') as arch:
            lineas = arch.readlines()
            for linea in lineas:
                valorTotal += int(linea.strip())
        return valorTotal