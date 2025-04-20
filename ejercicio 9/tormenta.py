class Tormenta:
    def __init__(self,nombre,intensidad,velocidad_viento,region):
        self.nombre = nombre
        self.set_intensidad(intensidad)
        self.set_velocidad_viento(velocidad_viento)
        self.region = region
    
    #errores
    def set_intensidad(self,intensidad):
        if intensidad < 1 or intensidad > 10:
            raise ValueError("Valor fuera de rango (1-10)")
        self.intensidad = intensidad
    
    def set_velocidad_viento(self,velocidad_viento):
        if velocidad_viento < 0:
            raise ValueError("Valor negativo ()")
        self.velocidad_viento = velocidad_viento
    
    #metodos de la clase
    def calcular_peligrosidad(self):
        peligrosidad = self.velocidad_viento * self.intensidad
        return peligrosidad

    def clasificar_tormenta(self):
        peligrosidad = self.calcular_peligrosidad()
        clasificacion = ""
        if peligrosidad < 250:
            clasificacion = "baja"
        elif peligrosidad >= 250 and peligrosidad < 500:
            clasificacion = "media"
        elif peligrosidad > 500:
            clasificacion = "alta"
        return clasificacion
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nIntensidad: {self.intensidad}\nVelocidad de viento: {self.velocidad_viento}\nRegion: {self.region}")
#<>