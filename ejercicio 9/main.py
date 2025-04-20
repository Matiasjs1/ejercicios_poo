from tormenta import Tormenta
from tormentaTropical import TormentaTropical
from tormentaElectrica import TormentaElectrica

def tormentas_peligrosidad(lista):
    listaB = list(lista)
    listaA = []
    while listaB:
        tormentaPeligrosa = listaB[0]
        for i in listaB:
            if i.calcular_peligrosidad() > tormentaPeligrosa.calcular_peligrosidad():
                tormentaPeligrosa = i
            listaA.append((tormentaPeligrosa,tormentaPeligrosa.calcular_peligrosidad()))
            listaB.remove(tormentaPeligrosa)
        return listaA
    
def agregar_tormenta_region(tormenta):
    if tormenta.region in tormentasRegion:
        tormentasRegion[tormenta.region].append(tormenta)
    else:
        tormentasRegion[tormenta.region] = []
        tormentasRegion[tormenta.region].append(tormenta)

def tormenta_mas_peligrosa(lista):
    tormentas_peligrosas = tormentas_peligrosidad(lista)
    tormenta_peligrosa = tormentas_peligrosas[0][0]
    return tormenta_peligrosa

def intensidad_segun_region(region):
    if region in tormentasRegion:
        intensidadTotal = 0
        for i in tormentasRegion[region]:
            intensidadTotal+=i.intensidad
        promedio = intensidadTotal/len(tormentasRegion[region])
    else:
        promedio = "La region no esta registrada"
    return promedio
    
def main():
    tormentas = []
    global tormentasRegion
    tormentasRegion = {}
    
    while True:
        opciones = int(input("Elija:\n1-Registrar tormenta\n2-Clasificar tormenta\n3-Listar tormentas segun peligrosidad\n4-Tormenta más peligrosa\n5-Promedio de intensidad segun region\n6-Salir\n"))
        while opciones < 1 or opciones > 5:
            print("ERROR")
            opciones = int(input("Elija:\n1-Registrar tormenta\n2-Clasificar tormenta\n3-Listar tormentas segun peligrosidad\n4-Tormenta más peligrosa\n5-Promedio de intensidad segun region\n6-Salir\n"))
        if opciones == 1:
            try:
                tipo = int(input("Tipo: 1-Normal 2-Tropical 3-Electrica: "))
                while tipo < 1 or tipo > 3:
                    print("ERROR")
                    tipo = int(input("Tipo: 1-Normal 2-Tropical 3-Electrica: "))
                nombre = str(input("Nombre: "))
                intensidad = int(input("Intensidad: "))
                velocidad_viento = int(input("Velocidad de viento: "))
                region = str(input("Region: "))
                if tipo == 1:
                    tormenta = Tormenta(nombre,intensidad,velocidad_viento,region)
                elif tipo == 2:
                    tormenta = TormentaTropical(nombre,intensidad,velocidad_viento,region)
                elif tipo == 3:
                    tormenta = TormentaElectrica(nombre,intensidad,velocidad_viento,region)
                tormentas.append(tormenta)
                agregar_tormenta_region(tormenta)
            except ValueError as e:
                print("Error: ",e)
        elif opciones == 2:
            if tormentas:
                x=0
                for i in tormentas:
                    x+=1
                    print(f"{x})")
                    i.mostrar_info()
                elegirTormenta = int(input("Que tormenta quiere clasificar? "))
                while elegirTormenta < 1 or elegirTormenta > len(tormentas):
                    print("ERROR")
                    elegirTormenta = int(input("Que tormenta quiere clasificar? "))
                tormenta = tormentas[elegirTormenta-1]
                print(tormenta.clasificar_tormenta())
            else:
                print("No hay tormentas registradas")
        elif opciones == 3:
            if tormentas:
                tormentas_peligrosas = tormentas_peligrosidad(tormentas)
                for i in tormentas_peligrosas:
                    print(f"{i[1]}")
                    print(f"{i[0].mostrar_info()}")
            else:
                print("No hay tormentas registradas")
        elif opciones == 4:
            if tormentas:
                tormenta_peligrosa = tormenta_mas_peligrosa(tormentas)
                print(tormenta_peligrosa.mostrar_info())
            else:
                print("No hay tormentas registradas")
        elif opciones == 5:
            if tormentas:
                regionPromedio = str(input("De que region desea saber el promedio de intensidad? "))
                print(intensidad_segun_region(regionPromedio))
            else:
                print("No hay tormentas registradas")
        elif opciones == 6:
            break

if __name__ == "__main__":
    main()

#<>