import os, multiprocessing as mp, time, random

def hijo_cuadrado(q, valor):
    cuadrado = valor.value**2
    q.put(cuadrado)

def hijo_cubo(q, valor):
    cuadrado = valor.value**3
    q.put(cuadrado)

def main():
    q = mp.Queue()
    value = mp.Value('i', 0)
    valor_usuario = int(input("Escriba un valor entero: "))
    value.value = valor_usuario
    p1 = mp.Process(target=hijo_cuadrado, args = (q, value))
    p2 = mp.Process(target=hijo_cubo, args = (q, value))

    p1.start()
    p1.join()
    p2.start()
    p2.join()
    
    print(f"El cuadrado de {valor_usuario} es: {q.get()}")
    print(f"El cubo de {valor_usuario} es: {q.get()}")
    print("Proceso finalizado")

if __name__ == "__main__":
    main()

# 4. Cálculo delegado a procesos hijos y comunicación con el proceso padre.
# Crear un programa en el que el proceso padre solicite al usuario un número
# entero. Luego debe delegar a dos procesos hijos el cálculo del cuadrado y del cubo
# del número, respectivamente.
# Los resultados deben ser comunicados al padre usando una cola (Queue) y
# luego mostrados por el padre en consola.