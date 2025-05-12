class Boxeador:
    def __init__(self, nombre, dni, edad, peso):
        self.nombre = nombre
        self.__dni = dni
        self.edad = edad
        self.peso = peso
        self.historial = []
        self.categoria = self.definirCategoria(peso)

    def definirCategoria(self, peso):   
        categoria_devolver = None
        if peso < 60:
            categoria_devolver = "liviano"
        elif peso >= 60 and peso < 80:
            categoria_devolver = "Mediano"
        elif peso > 80:
            categoria_devolver = "Pesado"
        return categoria_devolver
    
    def calcular_puntaje_total(self):
        pass

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nPeso: {self.peso} \nCategoria: {self.categoria} \n ")