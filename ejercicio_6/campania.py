class Campania:
    def __init__(self,cliente,presupuesto,duracion):
        self.cliente = cliente
        self.presupuesto = presupuesto
        self.duracion = duracion
        self.plataformas = []
        self.resultados = {}
    
    def registrar_resultados(self,dia,clics,conversiones,costo_dia):
        self.resultados[dia] = (clics,conversiones,costo_dia)
    
    def calcular_costo_total(self):
        costo_total = 0
        for i in self.resultados.values():
            costo_total += i[2]
        return costo_total

    def calcular_conversion_total(self):
        conversion_total = 0
        for i in self.resultados.values():
            conversion_total += i[1]
        return conversion_total
    
    def eficiencia(self):
        pass

    def mostrar_info(self):
        print(f"Cliente: {self.cliente}\nPresupuesto: {self.presupuesto}\nDuracion: {self.duracion}\nPlataformas:{self.plataformas}")