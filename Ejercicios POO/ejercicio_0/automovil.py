from vehiculo import Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, patente,nombre, dni):
        super().__init__(nombre,dni)
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.arranque = False
        self.__patente = patente ## el __ define el atributo como privado

    def get_patente(self):
        return self.__patente

    def set_patente(self, patente):
        self.__patente = patente
    
    #metodos específicos

    def mostra_info(self):
        print(f"Auto: {self.marca},{self.modelo},{self.anio}") #la f permite hacer un puntero de los atributos

    def arrancar(self):
        self.arranque = True
        print(f"Arranque: {self.arranque}")
    
    def apagar(self):
        self.arranque = False
        print(f"Arranque: {self.arranque}")