import random
import os
from naveEspacial import NaveEspacial
from astronauta import Astronauta
from errores import ErrorEspecialidad

def eventos():
    a = random.randint(1,10)
    danio = 0
    if a == 1:
        print("Se produjo una tormenta solar")
        danio = 25
    elif a == 2:
        print("Se produjo una falla tecnica")
        danio = 10
    elif a == 3:
        print("Se produjo una tormenta de meteoritos")
        danio = 80
    return danio

def main():
    astronautas = []
    recorridoPorDia = 10000
    recorrido = 0
    try:
        nombreNave = str(input("Ingrese el nombre de la nave: "))
        capacidadMax = int(input("Ingrese la capacidad máxima de tripulantes: "))
        combustible = int(input("Ingrese el combustible de la nave: "))
        nave = NaveEspacial(nombreNave, capacidadMax, combustible)
        distancia = int(input("Indique la distancia a recorrer durante la expedición (km): "))
        if distancia < 0:
            raise ValueError("La distancia no puede ser inferior a 0")
        if combustible < (distancia / 100):
            raise ValueError("No alcanza el combustible para la expedición")
    except ValueError as ve:
        print("Error: ",ve)
    try: 
        for i in range(0, nave.capacidadMax):
            print(f"Quedan {capacidadMax - len(astronautas)} lugares en la nave")
            opcion = int(input("Desea ingresar un astronauta: 1-Si 2-No: "))
            while opcion < 1 or opcion >2:
                print("Error")
                opcion = int(input("Desea ingresar otro astronauta: 1-Si 2-No: "))
            if opcion == 1:
                print("Inscribir Astronauta")
                try:
                    nombre = str(input("Ingrese el nombre: "))
                    edad = int(input("Ingrese la edad: "))
                    especialidad = str(input("Ingrese la especialidad: "))
                    astronautas.append(Astronauta(nombre, edad, especialidad))
                except ValueError as e:
                    print("Error: ",e)
            
            elif opcion == 2:
                break
        
        navegacion = False
        medicina = False
        mantenimiento = False
        for i in astronautas:
            if i.especialidad == "navegacion":
                navegacion = True
            elif i.especialidad == "medicina":
                medicina = True
            elif i.especialidad == "mantenimiento":
                mantenimiento = True

        if not navegacion or not medicina or not mantenimiento:
            raise ErrorEspecialidad()
    except ErrorEspecialidad  as e:
        print("Error: ", e)
    dias = 0
    while recorrido < distancia:
        dias += 1
        recorrido += recorridoPorDia
        if recorrido > distancia:
            recorrido = distancia
        nave.combustible -= recorrido/100
        print(f"Dia N°{dias}")
        danio = eventos()
        os.system("pause")

        for i in astronautas:
            afectado = random.choice([True,False])
            if afectado and i.salud > 0:
                i.recibirDanio(danio)
            elif not afectado and i.salud > 0:
                print(f"El astronauta {i.nombre} no recibió daño")
        os.system("pause")
    
    cantidadSobrevivientes = 0
    totalVida = 0
    for i in astronautas:
        if i.salud > 0:
            cantidadSobrevivientes += 1
            totalVida += i.salud
        else:
            astronautas.remove(i)
    if recorrido == distancia:
        destinoAlcanzado = "Alcanzado"
    else:
        destinoAlcanzado = "No alcanzado"

    print(f"Combustible restante: {nave.combustible}\nSalud Promedio: {(totalVida / cantidadSobrevivientes)}\n Destino: {destinoAlcanzado}")
    
if __name__ == "__main__":
    main()