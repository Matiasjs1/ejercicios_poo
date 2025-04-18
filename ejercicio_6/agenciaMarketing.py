class AgenciaMarketing:
    def __init__(self):
        self.campanias_activas = []
    
    def agregar_nuevas_campanias(self,campania):
        self.campanias_activas.append(campania)
    
    def listar_campania(self,tipo):
        listaTipo = []
        for i in self.campanias_activas:
            if i.tipo == tipo:
                listaTipo.append(i)
        return listaTipo

    def calcular_ranking_eficientes(self):
        listaA = []
        for i in self.campanias_activas:
            listaA.append((i.eficiencia(),i))
        return self.ordenar_lista(listaA)
        
    def ordenar_lista(self,lista):
        listaA = []
        while lista:
            eficienciaMax = lista[0]
            for i in lista:
                if i[0] > eficienciaMax[0]:
                    eficienciaMax = i
            listaA.append(eficienciaMax)
            lista.remove(eficienciaMax)
        return listaA

    def calcular_cliente_mejor_ROI(self):
        agenciaMax = self.campanias_activas[0]
        for i in self.campanias_activas: 
            if (i.calcular_conversion_total() * 10) / i.calcular_costo_total() > (agenciaMax.calcular_conversion_total() * 10) / agenciaMax.calcular_costo_total():
                agenciaMax = i
        return agenciaMax.cliente

    def campania_mayor_eficiencia(self):
        return self.calcular_ranking_eficientes()[0]

    def mostrar_informe(self):
        for i in self.campanias_activas:
            i.mostrar_info()