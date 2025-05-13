import multiprocessing
import os
import time
from gasto import Gasto
from ingreso import Ingreso
def gastos(q,gasto):
    pass

def ingresos(q,ingreso):
    pass
def main():
    gasto = Gasto()
    ingreso = Ingreso()
    while True:
        try:
            operacion = int(input("Que desea hacer:\n1-Ingresar Gasto\n2-Ingresar Ingreso\n3-Ver informe final (Termina el programa)\n"))
            if operacion < 1 or operacion > 3:
                raise ValueError("Se ingresó un valor inválido de operación") 
        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("Error: ",e)
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=gastos, args=(q,gasto))
    p2 = multiprocessing.Process(target=ingresos, args=(q,ingreso))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
if __name__ == "__main__":
    main()