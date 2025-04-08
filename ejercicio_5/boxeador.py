#nombre, DNI, edad, peso, historial de peleas (lista de tuplas) y categoría
class Boxeador:
    def __init__(self, dni, nombre, edad, peso):
        self.__dni = dni
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.historial = []
        self.categoria = self.definirCategoria(peso)
    
    def definirCategoria(self, peso):
        categoria_devolver = None
        if peso <60:
            categoria_devolver = "Liviano"
        elif peso >=60 and peso <80:
            categoria_devolver = "Mediano"
        elif peso >= 80:
            categoria_devolver = "Pesado"
        return categoria_devolver
    
    def calcular_puntaje_total(self):
        pass

    def mostrar_info(self):
         print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nPeso: {self.peso} \nCategoria: {self.categoria}")