import os, multiprocessing, time

def proceso_hijo(valor):
    print(f"Valor: {valor.value}")
    valor.value = 80
    #print(f"Valor: {valor.value}")

def main():
    valor = multiprocessing.Value('i', 0) #i para enteros
    p = multiprocessing.Process(target=proceso_hijo, args=(valor,))
    p.start()
    
    p.join()
    print(f"Padre vio el valor: {valor.value}")

if __name__ == '__main__':
    main()