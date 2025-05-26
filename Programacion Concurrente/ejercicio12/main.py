import multiprocessing as mp
import threading as th
from cajero import Cajero
import random
import os

lock = th.Lock()
lock2 = mp.Lock()


def cajero(lock2,id):
    with lock2:
        cuenta = Cajero(id)
        for _ in range(2):
            cl = th.Thread(target=cliente,args=(cuenta,lock))
            cl.start()
            cuenta.agregar_cliente(cl)
        for i in cuenta.clientes:
            i.join()
        cuenta.guardar_estado_final()
    

def cliente(cuenta, lock):
    with lock:
        for _ in range(5):
            opcion = random.randint(1,2)

            try:
                if opcion == 1:
                    valor = random.randint(0,1000)
                    cuenta.depositar(valor, os.getpid())
                    
                elif opcion == 2:
                    valor = random.randint(0,500)
                    cuenta.extraer(valor, os.getpid())
                
            except ValueError as ve:
                print("Error: ",ve)
            except Exception as e:
                print("Error: ",e)
            
def main():
    
    cj1 = mp.Process(target=cajero,args=(lock2,1))
    cj2 = mp.Process(target=cajero,args=(lock2,2))
    cj1.start()
    cj1.join()
    cj2.start()
    cj2.join()

if __name__ == "__main__":
    main()
#Simulá un banco donde hay varios cajeros (procesos) y cada cajero atiende
#a varios clientes (hilos). Cada cliente hace operaciones en una cuenta compartida
#(depósitos y extracciones). Protegé la cuenta con un Lock para evitar condiciones
#de carrera. Controlá si el saldo llega a negativo y lanzá una excepción que detenga
#al cliente. Imprimí un log con las operaciones y el estado final del saldo.

# <>