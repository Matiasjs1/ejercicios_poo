import os, multiprocessing

def proceso_hijo(q):
    q.put("Mensaje desde el hijo")
    q.put("Otro mensaje desde el hijo")

def main():
    print("Proceso padre")
    q = multiprocessing.Queue() #Metodo que le proporciona los atributos a q para que sea una cola. q va ser el proceso compartido entre padre e hijo
    p = multiprocessing.Process(target=proceso_hijo, args=(q,))
    
    p.start() #El start empieza a ejecutar al hijo.

    print(q.get()) #FIFO. Sale primero el que entro
    print(q.get()) #El segundo get muestra el siguiente mensaje, ya que el primero lo obtiene y lo libera de la cola

    p.join()
    
if __name__ == "__main__":
    main()