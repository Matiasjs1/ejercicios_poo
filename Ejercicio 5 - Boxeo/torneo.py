class Torneo:
    def __init__(self):
        self.boxeadores = []

    def agregar_boxeador(self, boxeador):
        self.boxeadores.append(boxeador)
        print("Se ha agregado un nuevo boxeador")

    def listar_boxeadores(self, categoriaListar):
        lista_devolver = []
            for i in self.boxeadores:
                if i.categoria == categoriaListar:
                    listaDevolver.append(i)
            return listaDevolver

    def promedio_edad(self, categoria)
        edadTotal = 0
        cantidad = 0
            for i in self.boxeadores:
                if i.categoria == categoriaListar:
                    edadTotal += i.edad 
                    cantidad ++
            return edadTotal/cantidad   
    
    def boxeadorMayorPuntaje(self):
        boxeadorMaximo = self.boxeadores[0]
        for i in self.boxeadores:
            if i.calcular_puntaje_total() > boxeadorMaximo.calcular_puntaje_total():
                boxeadorMaximo = i
        return i
    
    def listarRankingEficiencia(self):
        listaA = []
        for i in self.boxeadores:
            victorias = 0
            for x in i.historial:
                if x.[1] == "Victoria"
                    victorias ++
            eficiencia = victorias / len(i.historial)
            listaA.append((i, eficiencia))
        return self.ordenarLista(listaA)
        return listaA

    def ordenarLista(self, lista):
        pass
        
    def mostrarRankingGeneral(self):
        pass
