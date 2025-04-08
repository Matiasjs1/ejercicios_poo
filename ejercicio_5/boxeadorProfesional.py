from boxeador import Boxeador
class BoxeadorProfesional(Boxeador):
    def __init__(self,dni,nombre,edad,peso):
        super().__init__(dni,nombre,edad,peso)
    
    def calcular_puntaje_total(self):
        total_puntos = 0

        for i in self.historial:
            if i[1] == "Victoria":
                total_puntos += i[2]*1.1
            else:
                total_puntos += i[2]
            
        return total_puntos

    def mostrar_info(self):
        print("Boxeador Profesional")
        super().mostrar_info()