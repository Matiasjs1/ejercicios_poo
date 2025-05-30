from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, patente, nombre, dni): #__init__ es el constructor de Py
        super().__init__(nombre, dni)
        self.marca = marca  #self es el this de Python
        self.modelo = modelo 
        self.anio = anio
        self.arranque = False
        self.__patente = patente #"__" es para que el atributo sea privado

#Getter y Setter para la patenete (porque es privada)
    def get_patente(self): 
        return self.__patente

    def set_patente(self, patente):
        self.__patente = patente

#Metodos especificos 
    def mostra_info(self):
        print(f"Auto: {self.marca}, {self.modelo}, {self.anio}")#La "f" permite concatenar, ahorrandote los "+"
    
    def arrancar(self):
        self.arranque = True
        print(f"Arranque: {self.arranque}")
    
    def apagar(self):
        self.arranque = False
        print(f"Arranque: {self.apagar}")