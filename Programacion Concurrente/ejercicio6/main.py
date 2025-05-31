import multiprocessing as mp
import random
import time
from mago import Mago
from guerrero import Guerrero
import os

def log(mensaje):
    with open("registro_combate.txt", "a") as a:
        a.write(mensaje + "\n")

def proceso1(danio, vida, personaje, accion, evento, recibir):
    print(f"Proceso {os.getpid()} Listo")
    
    
    while True:
        print(f"Proceso {os.getpid()} Bloqueado")
        evento.clear()
        evento.wait()
        print(f"Proceso {os.getpid()} Listo")
        print(f"Proceso {os.getpid()} Ejecutandose")
        print(accion.value)
        if accion.value == 1:
            danio.put((personaje.atacar(),personaje.nombre))
            accion.value = 2
        elif accion.value == 2:
            vida.put((personaje.defenderse(recibir.get()), personaje.nombre))
            accion.value = 1
        elif accion.value == 3:
            break
    
    print(f"Proceso {os.getpid()} Terminado")
    
def main():
    danio = mp.Queue()
    vida = mp.Queue()
    recibir = mp.Queue()
    accion1 = mp.Value('i', 0)
    accion2 = mp.Value('i', 0)
    evento = mp.Event()
    peleadores = []

    while len(peleadores) < 2:
        while True:
            try:
                nombre1 = str(input("Ingrese el nombre del personaje: "))
                tipo = int(input("Ingrese el tipo del primer personaje: 1-Mago 2-Guerrero: "))
                if tipo != 1 and tipo !=2:
                    raise ValueError("El valor ingresado es inválido")
                if tipo == 1:
                    peleadores.append(Mago(nombre1))
                elif tipo == 2:
                    peleadores.append(Guerrero(nombre1))
                break
            except ValueError as ve:
                print("Error: ",ve)
            except Exception as e:
                print("Error: ",e)

    comienza = random.randint(0,1)
    if comienza == 0:
        accion1.value = 1
        accion2.value = 2
    else:
        accion1.value = 2
        accion2.value = 1
    
    p1 = mp.Process(target=proceso1,args=(danio, vida, peleadores[0], accion1, evento, recibir))
    p2 = mp.Process(target=proceso1,args=(danio, vida, peleadores[1], accion2, evento, recibir))
    p1.start()
    p2.start()

    time.sleep(1)
    evento.set()
    while True:
        danio_atacante, nombre_atacante = danio.get()
        recibir.put(danio_atacante)
        vida_defensor, nombre_defensor = vida.get()
        mensaje = f"{nombre_atacante} le infligió {danio_atacante} de daño a {nombre_defensor}\nLa vida de {nombre_defensor} es de {vida_defensor}"
        print(mensaje)
        log(mensaje)
        if vida_defensor == 0:
            accion1.value = 3
            accion2.value = 3
            ganador = nombre_atacante
            evento.set()
            break
        evento.set()
    
    p1.join()
    p2.join()
    
    mensaje = f"Terminó el combate\nEl ganador es {ganador}"
    print(mensaje)
    log(mensaje)

if __name__ == "__main__":
    main()
