class Propiedad:
    id_clase = 0
    def __init__(self, direccion, metros_cuadrados, ambientes, zona, precio_base, estado):
        Propiedad.id_clase +=1
        self.id_propiedad = Propiedad.id_clase
        self.direccion = direccion
        self.metros_cuadrados = metros_cuadrados
        self.ambientes = ambientes
        self.zona = zona
        self.precio_base = precio_base
        self.estado = estado

    
    def mostrar_info(self):
        print(f"Dirección: {self.direccion}\nMetros cuadrados: {self.metros_cuadrados}\nAmbientes: {self.ambientes}\nZona: {self.zona}\nPrecio base: {self.precio_base}\nEstado: {self.estado}")

    def calcularPrecioFinal(self):
        pass