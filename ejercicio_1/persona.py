class Persona:
    def __init__(self,nombre,edad,dni,licencia_conducir):
        self.nombre = nombre
        self.edad = edad
        self.__dni = dni
        self.licencia_conducir = licencia_conducir
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.__dni}")
    
    def puede_conducir(self):
        if self.licencia_conducir:
            print(f"{self.nombre} puede conducir")
        else:
            print(f"{self.nombre} no puede conducir")