class Boxeador:
    def __init__(self, nombre, dni, edad, peso):
        self.nombre = nombre
        self.nombre = nombre
        self.__dni = dni
        self.edad = edad
        self.peso = peso
        self.historial = []
        self.categoria = self.definirCategoria(peso)

    def definirCategoria(self, peso):
        categoriaDevolver = None
        if peso < 60:
            categoriaDevolver = "Liviano"
        elif peso >= 60 and peso <= 80:
            categoriaDevolver = "Mediano"
        elif peso > 80:
            categoriaDevolver = "Pesado"
        return categoriaDevolver
        
    def getDni(self):
        return self.__dni
    
    def setDni(self, dni):
        self.__dni = dni

    def calcular_puntaje_total(self):
        pass

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nPeso: {self.peso}\nCategoria: {self.categoria}")
