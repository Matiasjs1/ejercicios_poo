from propiedad import Propiedad

class PropiedadVenta(Propiedad):
    def __init__(self, direccion, metros_cuadrados, ambientes, zona, precio_base, estado, comision):
        super().__init__(direccion, metros_cuadrados, ambientes, zona, precio_base, estado)
        self.comision = comision
    
    def calcularPrecioFinal(self):
        precioFinal = self.precio_base + (self.precio_base*self.comision/100)
        return precioFinal