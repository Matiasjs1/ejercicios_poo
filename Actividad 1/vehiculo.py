from persona import Persona

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.conductor = None

    def asignar_conductor(self, conductor):
        if conductor.licencia_conducir and self.conductor == None:
            self.conductor = conductor
            print(f"Conductor: {self.conductor}")

    def mostrar_info(self):
        print(f"Info: {self.marca}, {self.modelo}, {self.anio}. {self.conductor}")