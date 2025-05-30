from excepcionImpresion import ExcepcionImpresion
import random
import time
class ImpresoraCompartida:
    def __init__(self, lock):
        self.lock = lock
    
    def imprimir(self):
        print(f"Esperando")
        with self.lock:
            rand = random.randint(0,1)
            if rand == 0:
                raise ExcepcionImpresion()
            print(f"Imprimiendo")
            time.sleep(2)
            print(f"Se imprimió el archivo")