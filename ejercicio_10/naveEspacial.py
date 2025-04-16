class NaveEspacial:
    def __init__(self,nombre, capacidadMax, combustible):
        self.nombre = nombre
        self.setCapacidadMax(capacidadMax)
        self.setCombustible(combustible)

    def setCombustible(self,combustible):
        if combustible < 0:
            raise ValueError("El combustible no puede ser negativo")
        self.combustible = combustible        


    def setCapacidadMax(self, capacidadMax):
        if capacidadMax < 1:
            raise ValueError("No se puede tener una capacidad menor a un tripulante")
        self.capacidadMax = capacidadMax
