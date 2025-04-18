from campania import Campania
class CampaniaSEO(Campania):
    def __init__(self, cliente, presupuesto, duracion):
        super().__init__(cliente, presupuesto, duracion)
        self.palabras_clave_efectivas = []
    
    def agregar_palabras_clave_efectivas(self, palabra):
        self.palabras_clave_efectivas.append(palabra)
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cantidad de palabras clave: {len(self.palabras_clave_efectivas)}")

    def eficiencia(self):
        return (self.calcular_conversion_total() / self.calcular_costo_total()) + len(self.palabras_clave_efectivas)