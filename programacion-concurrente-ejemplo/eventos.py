import os, multiprocessing, time

def proceso_hijo(evento):
    print("Hijo esperando el evento...")
    evento.wait() #wait porque esta esperando el evento q va a recibir. 
    #Sabe q como recurso compartido tiene una seccion de eventos
    print("Hijo recibió el evento")

def main():
    evento = multiprocessing.Event()
    p = multiprocessing.Process(target=proceso_hijo, args=(evento,))
    p.start()

    time.sleep(2) #Simula una vez creado al hijo el padre espera 2 segundos y lueg:
    print("Padre activa el evento") 
    evento.set() #se lo manda

    p.join() #join bloquea al padre y espera al hijo que finalize antes de que el finalize

if __name__ == '__main__':
    main()