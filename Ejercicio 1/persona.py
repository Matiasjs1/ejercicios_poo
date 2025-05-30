class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.__dni = dni
        self.licencia_conducir = None

    def mostrar_info(self):
        print(f"Nombre {self.nombre}, edad {self.edad}, dni {self.dni}, licencia de conducir {self.licencia_conducir}")

    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        self.dni = dni

    def puede_conducir(self):
        self.licencia_conducir = True