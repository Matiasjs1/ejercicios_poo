class Torneo:
    def __init__(self):
        self.boxeadores = []
    
    def agregar_boxeador(self, boxeador):
        self.boxeadores.append(boxeador)
        print("Se ha agregado un nuevo boxeador")
    def listar_boxeadores(self,categoriaListar):
        listaDevolver = []
        for i in self.boxeadores:
            if i.categoria == categoriaListar:
                listaDevolver.append(i)
        return listaDevolver

    def promedio_edad(self, categoriaListar):
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
        return boxeadorMaximo


    
    def listarRankingEficiencia(self):
        listaA = []
        for i in self.boxeadores: 
            victorias = 0
            for x in i.historial:
                if x[1] == "Victoria":
                    victorias++
            eficiencia = victorias / len(i.historial)
            listaA.append((i,eficiencia))
       
        return ordenarLista(listaA)

    def ordenarLista(self,lista):
        listaA = []
        while lista:
            mayor = lista[0]
            for i in lista:
                if i[1] > mayor[1]:
                    mayor = i
            listaA.append(mayor)
            lista.remove(mayor)
        return listaA

    def mostrarRankingGeneral(self):
        listaA = []
        for i in self.boxeadores:
            listaA.append((i, i.calcular_puntaje_total()))
        listaFinal = ordenarLista(listaA)
        for i in listaFinal:
            print(i.nombre, i[1])
        return listaFinal





#Mostrar ranking general, ordenado por puntaje.
