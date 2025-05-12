import time

class Servidor:
    def recibir_peticion(self, url, nombreCliente, lock):
        with lock:
            print("Cargando conexion...")
            time.sleep(2)
            print(f"Nombre del cliente: {nombreCliente}\nUrl: {url}")