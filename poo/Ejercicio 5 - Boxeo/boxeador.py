class Boxeador:
    def __init__ (self, nombre, dni, edad, peso):
        self.nombre = nombre
        self.__dni = dni
        self.setEdad(edad)
        self.peso = peso
        self.categoria = self.definirCategoria()
        self.historial = []

    def setEdad(self, edad):
        if edad < 12:
            raise ValueError("No se permiten menores de 12")
        set.edad = edad

    def getDni(self):
        return self.__dni
    
    def setDni(self, dni):
        self.__dni = dni

    def definirCategoria(self):
        categoria = None
        if self.peso < 60:
            categoria = "Liviano"
        elif self.peso >= 60 and self.peso <= 80:
            categoria = "Mediano"
        else:
            categoria = "Pesado"
        return categoria
    
    def calcular_puntaje_total(self):
        pass

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}\nDni: {self.getDni()}\nEdad: {self.edad}\nPeso: {self.peso}\nCategoria: {self.categoria}\nHistorial: {self.historial}")