import threading as th, random, time

lock = th.Lock()
saldo = 100

def retiro():
    global saldo
    if saldo >= 50:
        saldo -= 50
        print(f"Retiro exitoso | Saldo actual: ${saldo}")
    else:
        print(f"Retiro denegado | Saldo actual: ${saldo}")

def main():
    hilo1 = th.Thread(target=retiro)
    hilo2 = th.Thread(target=retiro)
    hilo3 = th.Thread(target=retiro)

    hilo1.start()
    time.sleep(2)
    hilo2.start()
    time.sleep(2)
    hilo3.start()
    time.sleep(2)

    hilo1.join()
    hilo2.join()
    hilo3.join()

if __name__ == "__main__":
    main()