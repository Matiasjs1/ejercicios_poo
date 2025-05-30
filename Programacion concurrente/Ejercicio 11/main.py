from impresoraCompartida import ImpresoraCompartida
from excepcionImpresion import ExcepcionImpresion
import threading as th
def hilo(impresora):
    try:
        impresora.imprimir()
    except ExcepcionImpresion as ei:
        print("Error: ",ei)
    except Exception as e:
        print("Error: ",e)

    print(f"Terminado")
    
def main():
    lock = th.Lock()
    impresora = ImpresoraCompartida(lock)
    h1 = th.Thread(target=hilo, args=(impresora,))
    h2 = th.Thread(target=hilo, args=(impresora,))

    h1.start()
    h2.start()
    h1.join()
    h2.join()

if __name__ == "__main__":
    main()