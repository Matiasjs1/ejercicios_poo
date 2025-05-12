class Persona:
    def __init__(self, nombre, edad, dni, licencia_conducir):
        self.nombre = nombre
        self.edad = edad
        self.__dni = dni
        self.licencia_conducir = licencia_conducir

    def mostrar_info(self):
        print(f"Info: {self.nombre}, {self.edad}, {self.__dni}")

    def puede_conducir(self):
        print(self.licencia_conducir)

