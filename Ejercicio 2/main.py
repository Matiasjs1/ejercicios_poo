from guerrero import Guerrero
from mago import Mago
from item import Item
import random
import os

if __name__ == "__main__":
    turno = 0
    danioTotal1 = 0
    danioTotal2 = 0
    numeroActivo = 1
    ##numeroActivo = random.randint(1,2)
    personaje1 = Mago("Mago Juan")
    personaje2 = Guerrero("Guerrero Pedro")
    espada1 = Item("Espada 3", "arma", 3)
    espada2 = Item("Espada 5", "arma", 5)
    escudo1 = Item("Escudo 3", "escudo", 3)
    pocion1 = Item("Pocion 20", "pocion", 20)
    personaje1.agregar_item(espada1)
    personaje1.agregar_item(pocion1)
    personaje2.agregar_item(espada2)
    personaje2.agregar_item(escudo1)

    while personaje1.vida > 0 and personaje2.vida > 0:
        turno +=1
        while numeroActivo == 1:
            os.system("cls")
            print("Turno del jugador 1")
            opcion = int(input("Seleccione una opcion: 1-Ver informacion 2-Usar Item 3-Atacar "))
            while opcion < 1 or opcion > 3:
                os.system("cls")
                print("Error")
                opcion = int(input("Seleccione una opcion: 1-Ver informacion 2-Usar Item 3-Atacar "))

            if opcion == 1:
                os.system("cls")
                print(f"Tu personaje: Nombre: {personaje1.nombre}, Vida: {personaje1.vida}, Ataque: {personaje1.ataque}, Defensa: {personaje1.defensa}")
                print(f"Personaje rival: Nombre: {personaje2.nombre}, Vida: {personaje2.vida}, Ataque: {personaje2.ataque}, Defensa: {personaje2.defensa}")
                os.system("pause")

            if opcion == 2:
                os.system("cls")
                numeroDeItem = 1
                print(f"(Si quiere salir presione 0)")
                if len(personaje1.inventario) == 0:
                    print("No tiene items disponibles")
                for i in personaje1.inventario:
                    print(f"{numeroDeItem}- {i.nombre}")
                    numeroDeItem +=1
                opcionItem = int(input("Seleccione una opción: "))
                while opcionItem < 0 or opcionItem > len(personaje1.inventario):
                    os.system("cls")
                    print("Error")
                    opcionItem = int(input("Seleccione el numero del item: "))
                if opcionItem == 0:
                    break
                personaje1.inventario[(opcionItem-1)].usar(personaje1)
                personaje1.inventario.pop((opcionItem-1))
                os.system("cls")
                print("Se han actualizado sus estadisticas")
                os.system("pause")
            
            if opcion == 3:
                os.system("cls")
                personaje1.atacar(personaje2)
                danioInfligido = personaje1.ataque - personaje2.defensa
                if danioInfligido < 0:
                    danioInfligido = 0
                danioTotal1 += danioInfligido
                print(f"Se le ha infligido {danioInfligido} de danio al rival")
                print(f"Vida acutal del rival: {personaje2.vida}")
                os.system("pause")
                numeroActivo = 2

        while numeroActivo == 2:
            os.system("cls")
            print("Turno del jugador 2")
            opcion = int(input("Seleccione una opcion: 1-Ver informacion 2-Usar Item 3-Atacar "))
            while opcion < 1 or opcion > 3:
                os.system("cls")
                print("Error")
                opcion = int(input("Seleccione una opcion: 1-Ver informacion 2-Usar Item 3-Atacar "))

            if opcion == 1:
                os.system("cls")
                print(f"Tu personaje: Nombre: {personaje2.nombre}, Vida: {personaje2.vida}, Ataque: {personaje2.ataque}, Defensa: {personaje2.defensa}")
                print(f"Personaje rival: Nombre: {personaje1.nombre}, Vida: {personaje1.vida}, Ataque: {personaje1.ataque}, Defensa: {personaje1.defensa}")
                os.system("pause")

            if opcion == 2:
                os.system("cls")
                numeroDeItem = 1
                print(f"(Si quiere salir inserte el número 0)")
                if len(personaje2.inventario) == 0:
                    print("No tiene items disponibles")
                for i in personaje2.inventario:
                    print(f"{numeroDeItem}- {i.nombre}")
                    numeroDeItem +=1
                opcionItem = int(input("Seleccione una opción: "))
                while opcionItem < 0 or opcionItem > len(personaje2.inventario):
                    os.system("cls")
                    print("Error")
                    opcionItem = int(input("Seleccione el numero del item: "))
                if opcionItem == 0:
                    break
                personaje2.inventario[(opcionItem-1)].usar(personaje2)
                personaje2.inventario.pop((opcionItem-1))
                os.system("cls")
                print("Se han actualizado sus estadisticas")
                os.system("pause")
            
            if opcion == 3:
                os.system("cls")
                personaje2.atacar(personaje1)
                danioInfligido = personaje2.ataque - personaje1.defensa
                if danioInfligido < 0:
                    danioInfligido = 0
                danioTotal2 += danioInfligido
                print(f"Se le ha infligido {danioInfligido} de danio al rival")
                print(f"Vida acutal del rival: {personaje1.vida}")
                os.system("pause")
                numeroActivo = 1
    os.system("cls")
    if personaje1.vida <= 0:
        print(f"El jugador 2 ha ganado!")
    elif personaje2.vida <= 0:
        print(f"El jugador 1 ha ganado!")
    print(f"La partida ha durado un total de {turno} turnos")
    print(f"Daño ingligido por el jugador 1 {danioTotal1}")
    print(f"Daño ingligido por el jugador 2 {danioTotal2}")
