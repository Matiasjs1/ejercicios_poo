from persona import Persona
class Vehiculo:
    def __init__(self,marca,modelo,anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.conductor = None
    
    def asignar_conductor(self, conductor):
        if conductor.licencia_conducir and self.conductor == None:
            self.conductor = conductor
            print(f"Conductor: {self.conductor.nombre}")
        else: 
            print("No puede ser conductor")
        
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")