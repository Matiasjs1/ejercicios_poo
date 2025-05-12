from boxeador import Boxeador

class BoxeadorProfesional(Boxeador):
    def __init__(self, nombre, dni, edad, peso):
        super().__init__(nombre, dni, edad, peso)
    
    def calcular_puntaje_total(self):
        puntajeTotal = 0
        for i in self.historial:
            if i[1] == "Victoria":
                puntajeTotal += i[2]* 1.1
            else:
                puntajeTotal += i[2]
        return puntajeTotal

    def mostrar_info(self):
        super().mostrar_info()
        print("Boxeador Profesional")











