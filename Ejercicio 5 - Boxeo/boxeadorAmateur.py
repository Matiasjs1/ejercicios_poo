from boxeador import Boxeador
class BoxeadorAmateur(Boxeador):
    def __init__ (self, nombre, dni, edad, peso):
        super().__init__(nombre, dni, edad, peso)

    def calcular_puntaje_total(self):
        total = 0
        for pelea in self.historial:
            total += pelea[2]
        return total
    
    def mostrarInfo(self):
        print("Boxeador Amateur")
        super().mostrarInfo()