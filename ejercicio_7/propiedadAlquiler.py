from propiedad import Propiedad
class PropiedadAlquiler(Propiedad):
    def __init__(self, id_propiedad, direccion, metros_cuadrados, ambientes, zona, precio_base,gastos_mensuales):
        super().__init__(id_propiedad, direccion, metros_cuadrados, ambientes, zona, precio_base)
        self.gastos_mensuales = gastos_mensuales
        self.tipo = "propiedad_alquiler"

    def calcular_precio_final(self):
        return self.precio_base + self.sumatoria(self.gastos_mensuales) #se puede usar sum directamente, solo que quise probar usar mi propio metodo