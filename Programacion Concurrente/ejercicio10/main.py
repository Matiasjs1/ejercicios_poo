from servidor import Servidor
import threading as th

lock = th.Lock()
servidor = Servidor()

def cliente(url, nombreCliente):
    global servidor
    global lock
    servidor.recibir_peticion(url, nombreCliente, lock)

def main():
    cliente1 = th.Thread(target=cliente, args=('https://youtube.com', 'Renzo Piris'))
    cliente2 = th.Thread(target=cliente, args=('https://instagram.com', 'Dario Guagliardo'))
    cliente3 = th.Thread(target=cliente, args=('https://twitch.tv', 'Matias Sesto'))
    cliente4 = th.Thread(target=cliente, args=('https://google.com', 'Facundo Chajade'))
    cliente5 = th.Thread(target=cliente, args=('https://x.com', 'Santiago Vallejos'))

    cliente1.start()
    cliente2.start()
    cliente3.start()
    cliente4.start()
    cliente5.start()

    cliente1.join()
    cliente2.join()
    cliente3.join()
    cliente4.join()
    cliente5.join()

    print("Fin de las conexiones")

if __name__ == "__main__":
    main()
