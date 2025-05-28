# 14.Monitor de Procesos Zombies
# Simular en Python una situación donde un sistema lanza múltiples procesos
# hijos que ejecutan tareas de corta duración, pero no todos son adecuadamente
# recogidos por el proceso padre, provocando la aparición de procesos zombies. Para
# lograrlo, se utilizará el módulo multiprocessing para crear varios procesos, y de
# manera intencionada se omitirá la llamada a join() en algunos de ellos.
# Además, implementará un hilo monitor, separado del flujo principal, cuya
# tarea será recorrer periódicamente la lista de procesos creados y verificar cuáles
# han finalizado su ejecución, pero aún no han sido recolectados. Este monitor
# actuará como un recolector de zombies, identificando estos procesos mediante el
# atributo exitcode y llamando a join() sobre ellos para liberar los recursos del
# sistema.
# La simulación debe generar una salida por consola que registre en qué
# momento un proceso finaliza, si queda en estado zombie, y cuándo es detectado y
# limpiado por el monitor. El objetivo es que el estudiante comprenda el ciclo de vida
# de un proceso, la diferencia entre estados activos y zombies, y cómo se puede
# implementar una estrategia de vigilancia y recolección automática en un sistema
# concurrente.
import multiprocessing as mp
import threading as th 
import time
import os



def proceso_hijo():
    print("Comienza la tarea")
    time.sleep(0.5)
    print("Terminó la tarea")

def monitor(lista):
    time.sleep(2)
    while lista:
        for proceso in lista:
            if proceso.is_alive() and proceso.exitcode is None:
                log(f"El proceso {proceso.pid} se detectó como zombie")
                proceso.join()
                lista.remove(proceso)
                log(f"El proceso {proceso.pid} ha finalizado por el monitor")
            
def log(mensaje):
    with open("registro.txt","a") as a:
        a.write(mensaje+"\n")

def main():
    lista = []
    for _ in range(5):
        proceso = mp.Process(target=proceso_hijo)
        proceso.start()
        lista.append(proceso)

    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i].join()
            lista.pop(i)

            log(f"El proceso {lista[i].pid} ha finalizado")
    return lista


if __name__ == "__main__":
    os.system("cls")

    lista = main()
    hilo_monitor = th.Thread(target=monitor,args=(lista,))
    hilo_monitor.start()
    hilo_monitor.join()