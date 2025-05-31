from campania import Campania
class CampaniaRedesSociales(Campania):
    def __init__(self, cliente, presupuesto, duracion):
        super().__init__(cliente, presupuesto, duracion)
        self.interacciones_sociales = {}
    
    def registrar_interacciones_sociales(self, dia, cantidad):
        self.interacciones_sociales[dia] = cantidad

    def mostrar_info(self):
        super().mostrar_info() 
        print("Interacciones sociales por dia: ")
        for i, a in self.interacciones_sociales.items():
            print(f"Dia {i}: {a}")

    def eficiencia(self):
        interaccionesTotales = 0
        for i in self.interacciones_sociales.values():
            interaccionesTotales += i
        return (self.calcular_conversion_total() + interaccionesTotales) / self.calcular_costo_total()
