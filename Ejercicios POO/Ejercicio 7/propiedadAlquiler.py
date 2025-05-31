from propiedad import Propiedad

class PropiedadAlquiler(Propiedad):
    def __init__(self, direccion, metros_cuadrados, ambientes, zona, precio_base, estado, expensas, impuestos, mantenimiento):
        super().__init__(direccion, metros_cuadrados, ambientes, zona, precio_base, estado)
        self.gastosMensuales = (expensas, impuestos, mantenimiento)
    
    def calcularPrecioFinal(self):
        totalGastosMensuales = 0
        for i in self.gastosMensuales:
            totalGastosMensuales += i
        precioFinal = self.precio_base + totalGastosMensuales
        return precioFinal
        