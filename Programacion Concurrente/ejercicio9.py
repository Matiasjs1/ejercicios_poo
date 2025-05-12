import threading as th, queue as q, time

cola = q.Queue()

def productor():
    for i in range(0,5):
        cola.put(i)
        print(f"Se genero el producto numero: {i}")

def consumidor():
    while not cola.empty():
        valor = cola.get()
        print(f"Se consumio el valor: {valor}")
        time.sleep(2)

def main():
    h1 = th.Thread(target=productor)
    h2 = th.Thread(target=consumidor)
    
    h1.start()
    h1.join()
    
    h2.start()
    h2.join()

    print("Termino el proceso padre")

if __name__ == "__main__":
    main()