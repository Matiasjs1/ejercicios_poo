import os
import multiprocessing as mp
import threading as th

def cliente(saldo, valor, opcion):
    if opcion == "depositar":
        saldo.value += valor


def cajero():
    saldo = mp.Value('f', 100.0)
    clientes = []
    clientes.append(th.Thread(target=cliente, args=(saldo,)))
    clientes.append(th.Thread(target=cliente, args=(saldo,)))
    clientes.append(th.Thread(target=cliente, args=(saldo,)))

def main():
    pass

if __name__ == "__main__":
    main()