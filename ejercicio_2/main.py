from item import Item
from guerrero import Guerrero
from mago import Mago
import os
import random
import time

if __name__ == "__main__":  
    def turno(jugador1,jugador2):
        print(f"Turno de {jugador1.nombre}")
        opcion = int(input("¿Que desea realizar? 1-Atacar 2-Usar un item: "))
        os.system("cls")
        if opcion == 1:
            jugador1.atacar(jugador2)
        if opcion == 2:
            if len(jugador1.inventario) == 0:
                while opcion == 2:
                    print("No tiene itemas para usar")
                    opcion = int(input("¿Que desea realizar? 1-Atacar 2-Usar un item: "))
                    os.system("cls")
                    if opcion == 1:
                        jugador1.atacar(jugador2)
            else:
                print("Elija entre sus items:")    
                
                for i in range(0,len(jugador1.inventario)):
                    print(f"""{i+1}-{jugador1.inventario[i].nombre}
    Tipo: {jugador1.inventario[i].tipo}
    Valor: {jugador1.inventario[i].valor}
                        """)
                opcionItem = (int(input()))
                opcionItem -= 1
                jugador1.inventario[opcionItem].usar(jugador1)

    ronda = 0
    item1 = Item("Poción de la vida", "pocion", 50) 
    item2 = Item("Espada del Rey Demonio", "arma", random.randint(1,10))
    item3 = Item("Escudo Legendario", "escudo", random.randint(1,10))

    mago1 = Mago("Sung")
    mago1.agregar_item(item1)
    mago1.agregar_item(item2)

    guerrero1 = Guerrero("Igris")
    guerrero1.agregar_item(item1)
    guerrero1.agregar_item(item3)

    print("Sung (Mago) vs Igris (Guerrero)")
    os.system("pause")
    os.system("cls")
    for i in range(0,3):
        print("Decidiendo quien empezará el combate.")
        time.sleep(0.5)
        os.system("cls")
        print("Decidiendo quien empezará el combate..")
        time.sleep(0.5)
        os.system("cls")
        print("Decidiendo quien empezará el combate...")
        time.sleep(0.5)
        os.system("cls")
    
    numRandom = random.randint(0,1)

    if numRandom == 0:
        jugadorA = mago1
        jugadorB = guerrero1
    elif numRandom == 1:
        jugadorA = guerrero1
        jugadorB = mago1
    
    print(f"Empieza: {jugadorA.nombre}")
    os.system("pause")
    while jugadorA.vida > 0 and jugadorB.vida > 0:
        ronda+=1
       
        os.system("cls")
        print(f"Ronda {ronda}")
        turno(jugadorA,jugadorB)
        jugadorA.mostrarStats()
        jugadorB.mostrarStats()
        os.system("pause")
        if jugadorB.vida == 0:
            break
        os.system("cls")
        print(f"Ronda {ronda}")
        turno(jugadorB,jugadorA)

        jugadorA.mostrarStats()
        jugadorB.mostrarStats()
        os.system("pause")
        
    if jugadorA.vida == 0:
        ganador = jugadorB
    else:
        ganador = jugadorA
        
    print(f"La batalla terminó. Ha ganado el jugador: {ganador.nombre}")