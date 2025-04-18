from campania import Campania
class CampaniaSEO(Campania):
    def __init__(self,cliente,presupuesto,duracion,palabras_clave_efectivas):
        super().__init__(cliente,presupuesto,duracion)
        self.palabras_clave_efectivas = palabras_clave_efectivas
        self.tipo = "SEO"
    
    def eficiencia(self):
        return self.calcular_conversion_total()/self.calcular_costo_total() * len(self.palabras_clave_efectivas)

    def mostrar_info(self):
        print("Campaña SEO")
        super().mostrar_info()
        print(f"Interacciones: {len(self.palabras_clave_efectivas)}")