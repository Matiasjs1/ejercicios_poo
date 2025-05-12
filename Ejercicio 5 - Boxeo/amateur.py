from boxeador import Boxeador

class Amateur(Boxeador):
    def __init__(self, nombre, dni, edad, peso):
        super().__init__(nombre, dni, edad, peso)

    
    def calcular_puntaje_total(self):
        total_puntos = 0
        for i in self.historial:
            total_puntos += i[2]
        return total_puntos

    def mostrar_info(self):
        print("Boxeador Amateur")
        super().mostrar_info()