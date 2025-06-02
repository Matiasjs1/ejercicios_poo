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
import threading as th
import multiprocessing as mp
import time
import os


def hijo():
    print(f"Inicio de tarea de corta duración {os.getpid()}")
    time.sleep(2)
    print(f"Fin de la tarea {os.getpid()}")

def monitor(hijos, procesos_finalizados):
    while len(hijos) != len(procesos_finalizados):
        for i in hijos:
            if i.exitcode != None and i not in procesos_finalizados:
                print(f"Proceso zombie detectado: {i.pid}")
                i.join()
                procesos_finalizados.append(i)
                print(f"Proceso zombie finalizado: {i.pid}")

if __name__ == "__main__":
    hijos = []
    procesos_finalizados = []
    for i in range(5):
        hijos.append(mp.Process(target=hijo))
        hijos[i].start()
    
    for a, i in enumerate(hijos):
        if a % 2 == 0:
            i.join()
            procesos_finalizados.append(i)
            print(f"Proceso finalizado correctamente: {i.pid}")
    
    print("Fin del proceso padre")

    hilo_monitor = th.Thread(target=monitor, args=(hijos,procesos_finalizados))
    hilo_monitor.start()
    hilo_monitor.join()