import multiprocessing
import os
import time

def proceso_hijo(q,value):
    cubo = value.value**3
    q.put(cubo)

def proceso_hijo2(q,value):
    cuadrado = value.value **2
    q.put(cuadrado)

def main():
    q = multiprocessing.Queue()
    value = multiprocessing.Value('i', 0)
    while True:
        try:
            valor = int(input("Ingrese el valor que quiere ver al cuadrado al cubo: "))
            break
        except Exception as e:
            print("Error: ",e)
    value.value = valor
    p1 = multiprocessing.Process(target=proceso_hijo, args=(q, value))
    p2 = multiprocessing.Process(target=proceso_hijo2, args=(q, value))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print(f"Cubo de {value.value}: {q.get()}")
    print(f"Cuadrado de {value.value}: {q.get()}")
if __name__ == "__main__":
    main()