

class Torneo:
    def __init__(self):
        self.boxeadores = []
    
    def agregarBoxeador(self, boxeador):
        self.boxeadores.append(boxeador)

    def listarBoxeador(self, categoria):
        listaA = []
        for i in self.boxeadores:
            if i.categoria == categoria:
                listaA.append(i)
        return listaA
    
    def calcularPromedioEdadCategoria(self, categoria):
        totalEdad = 0
        cantidad = 0
        for i in self.boxeadores:
            if i.categoria == categoria:
                totalEdad += i.edad
                cantidad += 1
        if cantidad != 0:
            return f"El promedio es de {totalEdad/cantidad}"
        else:
            return "No hay boxedores en la categoria"

    def rankingEficiencia(self):
        listaA = []
        for boxeador in self.boxeadores:
            contadorVictorias = 0
            for pelea in boxeador.historial:
                if pelea[1] == "Victoria":
                    contadorVictorias +=1
            eficiencia = contadorVictorias / len(boxeador.historial)
            listaA.append((boxeador,eficiencia))
        listaFinal = self.ordenarLista(listaA)
        return listaFinal
    
    def rankingGeneral(self):
        listaA = []
        for boxeador in self.boxeadores:
            puntaje = boxeador.calcular_puntaje_total()
            listaA.append((boxeador,puntaje))
        listaFinal = self.ordenarLista(listaA)
        return listaFinal

    def boxeadorMasPuntaje(self):
        lista = self.rankingGeneral()
        boxeador = lista[0][0]
        return boxeador

    def ordenarLista(self,lista):
        listaA = []
        while len(lista) != 0:
            mayor = lista[0]
            for tupla in lista:
                if tupla[1] > mayor[1]:
                    mayor = tupla
            listaA.append(mayor)
            lista.remove(mayor)
        return listaA
    
