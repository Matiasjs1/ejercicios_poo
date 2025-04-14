from errores import ValoresFueraRango, ValoresNegativos

class Tormenta:
    def __init__ (self, nombre, intensidad, velocidadViento, region):
        if intensidad < 1 or intensidad > 10:
            raise ValoresFueraRango()
        if velocidadViento < 0:
            raise ValoresNegativos()
        
        self.nombre = nombre
        self.intensidad = intensidad        
        self.velocidadViento = velocidadViento
        self.region = region

    def calcularPeligrosidad(self,total):
        if total <= 15:
            peligrosidad = "Baja"
        elif total > 15 and total < 20 :
            peligrosidad = "Media"
        elif total >= 20:
            peligrosidad = "Alta"
        return peligrosidad

    def calcularValorPeligrosidad(self):
        total = (self.velocidadViento / 10) + self.intensidad
        return total

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}, Intensidad: {self.intensidad}, Velocidad: {self.velocidadViento}, Region: {self.region}")
#<>