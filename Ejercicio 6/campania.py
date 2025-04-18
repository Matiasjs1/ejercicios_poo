class Campania:
    def __init__(self, cliente, presupuesto, duracion):
        self.cliente = cliente
        self.presupuesto = presupuesto
        self.duracion = duracion
        self.plataformas =[]
        self.resultados = {}

    def registrar_resultado(self, dia, clicks, conversiones, costo_dia):
        self.resultados[dia] = (clicks, conversiones, costo_dia)
    
    def calcular_costo_total(self):
        total = 0
        for i in self.resultados.values():
            total += i[2]
        return total

    def calcular_conversion_total(self):
        total = 0
        for i in self.resultados.values():
            total += i[1]
        return total


    def mostrar_info(self):
        print(f"Cliente: {self.cliente}\nPresupuesto (usd): {self.presupuesto}\nDuracion (días): {self.duracion}\nCosto total acutal: {self.calcular_costo_total()}\nConversion Total {self.calcular_conversion_total()}")

    def eficiencia(self):
        pass