import multiprocessing
import os
import time

def proceso_hijo():
    print(f"Proceso Nuevo ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso Listo ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso En Ejecución ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso Bloqueado ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso Suspendido ({os.getpid()})")
    time.sleep(5)
    print(f"Proceso Listo ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso En Ejecución ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso Terminado ({os.getpid()})")

def proceso_hijo2(event):
    print(f"Proceso Nuevo ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso Listo ({os.getpid()})")
    time.sleep(1)
    print(f"Proceso En Ejecución ({os.getpid()})")
    print(f"Se despausará el proceso Padre: {os.getppid()}")
    time.sleep(4)
    event.set()
    print(f"Proceso Terminado ({os.getpid()})")

def main():
    event = multiprocessing.Event()
    p1 = multiprocessing.Process(target=proceso_hijo)
    p2 = multiprocessing.Process(target=proceso_hijo2, args=(event,))
    p1.start()
    p2.start()
    event.wait()
    print(f"El evento padre {os.getpid()} se despauso")
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()

#Nuevo → Listo → En ejecución → Suspendido → Listo → En ejecución → Terminado.