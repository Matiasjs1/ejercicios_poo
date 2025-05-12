import threading as th
import time

def lavar_platos():
    print("Lavando platos")
    time.sleep(1)
    print("Estado: FINISH")

def barrer_piso():
    print("Barriendo piso")
    time.sleep(2)
    print("Estado: FINISH")

def cocinar():
    print("Cocinando")
    time.sleep(3)
    print("Estado: FINISH")

def main():
    hilo1 = th.Thread(target=lavar_platos)
    hilo2 = th.Thread(target=barrer_piso)
    hilo3 = th.Thread(target=cocinar)

    hilo1.start()
    hilo2.start()
    hilo3.start()
    
    hilo1.join()
    hilo2.join()
    hilo3.join()

    print("Todas las tareas estan FINISH")

if __name__ == "__main__":
    main()