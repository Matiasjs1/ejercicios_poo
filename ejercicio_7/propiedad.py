class Propiedad:
    def __init__(self,id_propiedad,direccion,metros_cuadrados,ambientes,zona,precio_base):
        self.__id_propiedad = id_propiedad
        self.direccion = direccion
        self.metros_cuadrados = metros_cuadrados
        self.ambientes = ambientes
        self.zona = zona
        self.precio_base = precio_base
        self.estado = "disponible"
        self.tipo = None
    
    def get_id_propiedad(self):
        return self.__id_propiedad
    
    def calcular_precio_final(self):
        pass
    
    def sumatoria(self,conjunto):
        sumatoria = 0
        for i in conjunto:
            sumatoria+=i
        return sumatoria
    
    def mostrar_info(self):
        print(f"ID Propiedad: {self.__id_propiedad}\nDirección: {self.direccion}\nMetros cuadrados: {self.metros_cuadrados}\nAmbientes: {self.ambientes}\nZona: {self.zona}\nPrecio base: {self.precio_base}\nEstado: {self.estado}")