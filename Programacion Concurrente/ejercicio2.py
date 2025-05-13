import os
import time
import multiprocessing
import random

def proceso_hijo():
    print(f"Proceso Nuevo ({os.getpid()})")
    time.sleep(random.randint(0,4))
    print(f"Proceso Listo ({os.getpid()})")
    time.sleep(random.randint(0,4))
    print(f"Proceso En Ejecución ({os.getpid()})")
    time.sleep(random.randint(0,4))
    print(f"Proceso Bloqueado ({os.getpid()})")
    time.sleep(random.randint(0,4))
    print(f"Proceso Listo ({os.getpid()})")
    time.sleep(random.randint(0,4))
    print(f"Proceso En Ejecución ({os.getpid()})")
    time.sleep(random.randint(0,4))
    print(f"Proceso Terminado ({os.getpid()})")
    
def main():
    p1 = multiprocessing.Process(target=proceso_hijo)
    p2 = multiprocessing.Process(target=proceso_hijo)
    p3 = multiprocessing.Process(target=proceso_hijo)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
if __name__ == "__main__":
    main()




# 2. Simulación del cambio de estado de procesos
# Simular mediante un programa en Python el ciclo de vida de tres 
# procesos hijos, representando los siguientes estados: 
# Nuevo → Listo → En ejecución → Bloqueado → Listo → Terminado.
# Cada proceso debe mostrar en consola su transición por los estados
# utilizando print() y simular el tiempo de ejecución de cada
# estado usando time.sleep() con duraciones aleatorias.