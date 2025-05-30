import os
import time
import multiprocessing

def proceso_hijo1():
    print(f"Proceso hijo: PID = {os.getpid()}, Padre = {os.getppid()}")
    time.sleep(2)
    print("Proceso hijo finalizado")

def proceso_hijo2():
    print(f"Proceso hijo: PID = {os.getpid()}, Padre = {os.getppid()}")
    time.sleep(2)
    print("Proceso hijo finalizado")

def proceso_hijo3():
    print(f"Proceso hijo: PID = {os.getpid()}, Padre = {os.getppid()}")
    time.sleep(2)
    print("Proceso hijo finalizado")



def main():
    print("Hola - ")
    print(f"Proceso padre: PID = {os.getpid()}") #os.getpid() permite acceder a la id del proceso

    #creando proceso hijo
    p1 = multiprocessing.Process(target=proceso_hijo1)
    p1.start() #Iniciar el proceso p
    p2 = multiprocessing.Process(target=proceso_hijo1)
    p2.start() #Iniciar el proceso p
    p3 = multiprocessing.Process(target=proceso_hijo1)
    p3.start() #Iniciar el proceso p



    print(f"Proceso padre creó un hijo con PID = {p1.pid}")
    print(f"Proceso padre creó un hijo con PID = {p2.pid}")
    print(f"Proceso padre creó un hijo con PID = {p3.pid}")


    p1.join() #esperar que el hijo termine. Sino, el hijo podria no ejecutarse. El padre pasa a bloqueado y el hijo a ejecutado
    p2.join()
    p3.join()


    print("Proceso padre finalizado")

if __name__ == '__main__':
    main()