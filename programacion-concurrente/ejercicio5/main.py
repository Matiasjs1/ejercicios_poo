import os, time, multiprocessing as mp, random
from gastos import Gasto
from ingresos import Ingreso

def leer_gastos(q):
    print(f"Proceso listo {os.getpid()}")
    time.sleep(2)
    print(f"Proceso ejecutando {os.getpid()}")
    gastos = Gasto("gastos.txt")
    time.sleep(2)
    print(f"Proceso bloqueado {os.getpid()}")
    time.sleep(2)
    print(f"El proceso {os.getpid()} se ha desbloqueado")
    q.put(gastos.calcular_total())

def leer_ingresos(q):
    print(f"Proceso listo {os.getpid()}")
    time.sleep(2)
    print(f"Proceso ejecutando {os.getpid()}")
    time.sleep(2)
    ingresos = Ingreso("ingresos.txt")
    print(f"Proceso bloqueado {os.getpid()}")
    time.sleep(2)
    print(f"El proceso {os.getpid()} se ha desbloqueado")
    q.put(ingresos.calcular_total())

def log(archivo, mensaje):
    with open(archivo, 'a') as arch:
        arch.write(f"{mensaje}\n")

def main():
    q = mp.Queue()
    proceso_gastos = mp.Process(target=leer_gastos, args=(q,))
    proceso_ingresos = mp.Process(target=leer_ingresos, args=(q,))
    while True:
        try: 
            accion = int(input("¿Que desea hacer? 1- Gastos, 2- Ingresos, 3- Salir"))
            if accion < 1 or accion > 3:
                raise ValueError("Ingrese un valor valido")

            if accion == 1:
                num = int(input("Ingrese el valor: "))
                log('gastos.txt', num)

            elif accion == 2:
                num = int(input("Ingrese un valor: "))
                log('ingresos.txt', num)

            elif accion == 3:
                break

        except ValueError as e:
            print("Error: ", e)
    
    try: 
        proceso_gastos.start()
        proceso_gastos.join()
        proceso_ingresos.start()
        proceso_ingresos.join()
    except FileNotFoundError as fe:
        print("Error: ", fe)

    gastos = q.get()
    ingresos = q.get()

    log('balance_final.txt', ingresos - gastos)
if __name__ == "__main__":
    main()