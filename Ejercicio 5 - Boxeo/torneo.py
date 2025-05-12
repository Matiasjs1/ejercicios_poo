class Torneo:
    def __init__ (self):
        boxeadores = []

    def agregarBoxeadores(self, boxeador):
        self.boxeadores.append(boxeador)
        print(f"El boxeador {boxeador.nombre} fue agregado al torneo")
    
    def listarCategoria(self, categoria):
        listaA = []
        for boxeador in self.boxeadores:
            if boxeador.categoria == categoria:
                listaA.append(boxeador)
        return listaA
    
    def promedioEdad(self):
        edades = 0
        cantidad = 0
        for boxeador in self.boxeadores:
            cantidad += 1
            edades += boxeador.edad
        if cantidad != 0:
            return f"El promedio de edades es de: {edades / cantidad}"
        else:
            raise ValueError("No hay boxeadores en la categoria")

    def boxeadorMaximo(self):
        boxeadorMax = self.boxeadores[0]
        for boxeador in self.boxeadores:
            if boxeadorMax.calcular_puntaje_total() < boxeador.calcular_puntaje_total():
                boxeadorMax = boxeador
        return f"El boxeador de mayor puntaje es {boxeadorMax.nombre} con un total de {boxeadorMax.calcular_puntaje_total()} PTS"
    
    def listarRankingEficiencia(self):
        listaA = []
        for boxeador in self.boxeadores:
            cantidadVictorias = 0
            for pelea in boxeador.historial:
                if pelea[1] == "Victoria":
                    cantidadVictorias += 1
            eficiencia = cantidadVictorias / len(boxeador.historial)
            listaA.append((boxeador, eficiencia))
        listaFinal = self.ordenarLista(listaA)
        return listaFinal
    
    def rankingGeneral(self):
        listaA = []
        for boxeador in self.boxeadores:
            puntaje = boxeador.calcular_puntaje_total()
            listaA.append((boxeador, puntaje))
        listaFinal = self.ordenarLista(listaA)
        return listaFinal

    def ordenarLista(self, lista):
        listaA = []
        while lista:
            mayor = lista[0]
            for tupla in lista:
                if tupla[1] > mayor[1]:
                    mayor = tupla
            listaA.append(mayor)
            lista.remove(mayor)
        return listaA