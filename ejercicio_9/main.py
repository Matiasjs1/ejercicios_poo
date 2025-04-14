from tormenta import Tormenta
from tormentaTropical import TormentaTropical
from tromentaElectrica import TormentaElectrica
from errores import ValoresFueraRango, ValoresNegativos
import os

def listarTormentaPeligrosidad(lista, peligrosidad):
    listaA = []
    for i in lista:
        if i[0].calcularPeligrosidad(i[0].calcularValorPeligrosidad()) == peligrosidad:
            listaA.append((i[0], peligrosidad))
    return listaA

def calcularTormentaMaxima(lista):
    tormentaMayor = lista[0]
    for i in lista:
        if tormentaMayor[1] < i[1]:
            tormentaMayor = i
    return tormentaMayor[0]

if __name__ == "__main__":
    tormentasRegion = {}
    listaTormentas = []

    while True:
        try: 
            opcion = int(input("Seleccione una opcion: 1-Ingresar Tormenta, 2-Listar Tormentas, 3-Promedio de intensidad por Region 4-Mostrar Tormenta más Peligrosa 5-Salir "))
            if opcion < 1 or opcion > 5:
                raise ValueError("Valor fuera de rango")
        except ValueError as e:
            os.system("cls")
            print("Error: ",e)
            os.system("pause")
            continue

        if opcion == 1:
            try:
                elegirTipoTormenta = int(input("1- Normal, 2- Tropical, 3- Electrica: "))
                if elegirTipoTormenta < 1 or elegirTipoTormenta > 3:
                    raise ValueError("Valor fuera de rango")
            except ValueError as e:
                os.system("cls")
                print("Error: ",e)
                os.system("pause")
                continue
            
            nombreTormenta = str(input("Ingrese el nombre: "))
            intensidadTormenta = int(input("Ingrese la intensidad: "))
            velocidadTormenta = int(input("Ingrese la velocidad: "))
            regionTormenta = str(input("Ingrese la region: "))
            
            try:
                if regionTormenta not in tormentasRegion:
                    tormentasRegion[regionTormenta] = []
                    tormentaCreada = None
                if elegirTipoTormenta == 1:
                    tormentaCreada = Tormenta(nombreTormenta, intensidadTormenta, velocidadTormenta, regionTormenta)
                elif elegirTipoTormenta == 2:
                    tormentaCreada = TormentaTropical(nombreTormenta, intensidadTormenta, velocidadTormenta, regionTormenta)
                elif elegirTipoTormenta == 3:
                    tormentaCreada = TormentaElectrica(nombreTormenta, intensidadTormenta, velocidadTormenta, regionTormenta)
                tormentasRegion[regionTormenta].append(tormentaCreada)
                listaTormentas.append((tormentaCreada, tormentaCreada.calcularValorPeligrosidad()))
            except (ValoresFueraRango, ValoresNegativos) as e:
                os.system("cls")
                print("Error: ",e)
                os.system("pause")
                continue
                
        elif opcion == 2:
            try:
                opcionPeligrosidad = int(input("Que lista de peligrosidad quiere: 1-Baja 2-Media 3-Alta: "))
                if opcionPeligrosidad < 1 or opcionPeligrosidad > 3:
                    raise ValueError("Valor fuera de rango")
            except ValueError as e:
                os.system("cls")
                print("Error: ",e)
                os.system("pause")
                continue
            lista = None
            if opcionPeligrosidad == 1:
                lista = listarTormentaPeligrosidad(listaTormentas, "Baja")
            elif opcionPeligrosidad == 2:
                lista = listarTormentaPeligrosidad(listaTormentas, "Media")
            elif opcionPeligrosidad == 3:
                lista = listarTormentaPeligrosidad(listaTormentas, "Alta")
            for i in lista:
                i[0].mostrarInfo()
                
        elif opcion == 3:
            try:
                regionElegida = str(input("De qué región quiere sacar un promedio de intensidad: }"))
                if regionElegida not in tormentasRegion:
                    raise ValueError("El valor no se encuentra en las regiones registradas")
            except ValueError as e:
                os.system("cls")
                print("Error: ",e)
                os.system("pause")
                continue

            cantidadTormentas = 0
            total = 0
            
            for i in tormentasRegion[regionElegida]:
                cantidadTormentas +=1
                total += i.intensidad
            promedio = total / cantidadTormentas
            print(f"El promedio en la region {regionElegida} es de: {promedio}")
        
        elif opcion == 4:
            if len(listaTormentas) != 0:
                calcularTormentaMaxima(listaTormentas).mostrarInfo()
            else:
                print("No hay tormentas registradas")

        elif opcion == 5:
            break