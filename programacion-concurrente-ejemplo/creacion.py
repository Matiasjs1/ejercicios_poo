import os
import time
import multiprocessing

def proceso_hijo():
    print(f"Proceso hijo: PID = {os.getpid()}, Padre = {os.getppid()}")
    time.sleep(2)
    print("Proceso hijo finalizado")

def main():
    print("Hola - ")
    print(f"Proceso padre: PID = {os.getpid()}") #os.getpid() permite acceder a la id del proceso

    #creando proceso hijo
    p = multiprocessing.Process(target=proceso_hijo)
    p.start() #Iniciar el proceso p

    print(f"Proceso padre creó un hijo con PID = {p.pid}")

    p.join() #esperar que el hijo termine. Sino, el hijo podria no ejecutarse. El padre pasa a bloqueado y el hijo a ejecutado

    print("Proceso padre finalizado")

if __name__ == '__main__':
    main()