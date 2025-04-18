from campania import Campania
class CampaniaRedesSociales(Campania):
    def __init__(self,cliente,presupuesto,duracion,interacciones_sociales):
        super().__init__(cliente,presupuesto,duracion)
        self.interacciones_sociales = interacciones_sociales
        self.tipo = "redes_sociales"

    def eficiencia(self):
        return (self.calcular_conversion_total()+len(self.interacciones_sociales))/self.calcular_costo_total()


    
    def mostrar_info(self):
        print("Campaña Redes Sociales")
        super().mostrar_info()
        print(f"Interacciones: {self.interacciones_sociales}")