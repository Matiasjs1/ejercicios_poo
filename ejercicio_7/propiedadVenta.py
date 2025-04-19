from propiedad import Propiedad
class PropiedadVenta(Propiedad):
    def __init__(self, id_propiedad, direccion, metros_cuadrados, ambientes, zona, precio_base,comision):
        super().__init__(id_propiedad, direccion, metros_cuadrados, ambientes, zona, precio_base)
        self.comision = comision
        self.tipo = "propiedad_venta"

    def calcular_precio_final(self):
        return self.precio_base + self.comision*100/self.precio_base

    