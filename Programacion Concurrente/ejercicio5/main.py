import multiprocessing
import os
from gasto import Gasto
from ingreso import Ingreso
def gastos(q, valorGasto, operacion):
    _gasto = Gasto()
    if operacion.value == 1:
        _gasto.agregar_gasto(valorGasto.value)
    elif operacion.value == 3:
        q.put(_gasto.calcular_total())

def ingresos(q, valorIngreso, operacion):
    _ingreso = Ingreso()
    if operacion.value == 2:
        _ingreso.agregar_ingreso(valorIngreso.value)
    elif operacion.value == 3:
        q.put(_ingreso.calcular_total())
def main():
    balance_final = "balance_final.txt"
    valor1 = multiprocessing.Value('f', 0)
    valor2 = multiprocessing.Value('f', 0)
    q = multiprocessing.Queue()
    seguir = True
    while True:
        try:
            seguir = int(input("Quiere realizar una operación: 1-Si, 2-No: "))
            if seguir !=1 and seguir != 2:
                raise ValueError("Valor invalidos")
            if seguir == 2:
                break
            elif seguir == 1:
                os.system("cls")
        except Exception as e:
            print("Error: ",e)
        
        while seguir:
            try:
                operacion = int(input("Que desea hacer:\n1-Ingresar Gasto\n2-Ingresar Ingreso\n3-Ver informe final (Termina el programa)\n"))
                if operacion < 1 or operacion > 3:
                    raise ValueError("Se ingresó un valor inválido de operación") 
                valor2.value = operacion
                if operacion == 1:
                    valor1.value = float(input("Ingreso de gasto: "))
                    p1 = multiprocessing.Process(target=gastos, args=(q,valor1,valor2))
                    p1.start()
                    p1.join()

                elif operacion == 2:
                    valor1.value = float(input("Monto de Ingreso: "))
                    p2 = multiprocessing.Process(target=ingresos, args=(q,valor1,valor2))
                    p2.start()
                    p2.join()
                
                elif operacion == 3:
                    p2 = multiprocessing.Process(target=ingresos, args=(q,valor1,valor2))
                    p1 = multiprocessing.Process(target=gastos, args=(q,valor1,valor2))
                    p2.start()
                    p2.join()
        
                    p1.start()
                    p1.join()

                    ingresos_final = q.get()
                    gastos_final = q.get()
                    with open(balance_final, "w") as archivo:
                        archivo.write(f"{ingresos_final - gastos_final}")
                    seguir = False
                    
                break
            except ValueError as ve:
                print("Error:", ve)
            except Exception as e:
                print("Error: ",e)
        
if __name__ == "__main__":
    main()