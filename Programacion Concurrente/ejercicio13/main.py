import threading as th
import random
from buffer import Buffer
import os
cantidad_errores = 0
def productor(buffer):
    rango = random.randint(0,9)
    if rango == 9:
        valor = "TROLEADOR CARA"
    else:
        valor = random.randint(1,100)
    buffer.producir(valor)

def consumidor(buffer):
    global cantidad_errores
    while True:
        try:
            buffer.consumir()
            break
        except TypeError as te:
            print("Error: ", te)
            buffer.registro("errores.txt","Hubo un error al consumir el dato")
            cantidad_errores +=1
        except Exception as e:
            print("Error: ", e)
            cantidad_errores +=1

def main():
    buffer = Buffer()
    productores = []
    consumidores = []
    for _ in range(5):
        productores.append(th.Thread(target=productor,args=(buffer,)))
    for _ in range(3):
        consumidores.append(th.Thread(target=consumidor,args=(buffer,)))

    for i in productores:
        i.start()
    for i in consumidores:
        i.start()

    for i in productores:
        i.join()
    for i in consumidores:
        i.join()
    
    with open("registro_final.txt", "a") as archivo_final:
        archivo_final.write("VALORES INGRESADOS:\n")
        with open("valores_ingresados.txt", "r") as archivo_productor:
            lineas = archivo_productor.readlines()
            for linea in lineas:
                archivo_final.write(f"{linea.strip()}\n")
        archivo_final.write("VALORES PROCESADOS:\n")
        with open("valores_procesados.txt", "r") as archivo_consumidor:
            lineas = archivo_consumidor.readlines()
            for linea in lineas:
                archivo_final.write(f"{linea.strip()}\n")
        archivo_final.write(f"Hubo una cantidad de {buffer.esperas} esperas")
        archivo_final.write("\nERRORES:\n")
        if os.path.exists("errores.txt"):
            with open("errores.txt", "r") as archivo_errores:
                lineas = archivo_errores.readlines()
                for linea in lineas:
                    archivo_final.write(f"{linea.strip()}\n")
        else:
            archivo_final.write(f"No hubieron errores\n")
        archivo_final.write(f"Cantidad de veces que falló y continuó el programa: {cantidad_errores}:")
        
if __name__ == "__main__":
    main()