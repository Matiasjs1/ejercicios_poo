from persona import Persona

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.conductor = None

    def asignar_conductor(self, conductor):
        self.conductor = conductor
    
    def mostrar_info(self):
        if self.conductor != None:
            print(f"Marca {self.marca}, modelo {self.modelo}, año {self.anio}, conductor: {self.conductor.nombre}")
        else:
            print(f"Marca {self.marca}, modelo {self.modelo}, año {self.anio}, conductor: Sin conductor")
    