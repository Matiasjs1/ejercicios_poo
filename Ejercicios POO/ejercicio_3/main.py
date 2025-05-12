from camion import Camion
from motocicleta import Motocicleta
from automovil import Automovil

def registrarDiccionario(diccionario, vehiculo):
    diccionario[vehiculo.matricula] = {vehiculo.datos}
    
def registrarLista(lista, vehiculo):
    lista.append(vehiculo)
    

if __name__ == "__main__":
    camion1 = Camion("AAAA",13)
    moto1 = Motocicleta("AAAB",14)
    auto1 = Automovil("AAAC", 15)
    salir = False
    vehiculos = {}
    registros = []
    total_ingresos = 0


    salir = False

    while not salir:
        opciones = int(input("Elija una opción: 1-Registrar entrada 2-Registrar Salida 3-Ver información vehículo 4-Salir "))
        while opciones < 1 or opciones > 4:
            print("Error")
            opciones = int(input("Elija una opción: 1-Registrar entrada 2-Registrar Salida 3-Ver registros 4-Salir "))
        
        if opciones == 1:
            vehiculo = int(input("¿Qué tipo de vehículo ingresó? 1-Camion 2-Automovil 3-Motocicleta: "))
            while vehiculo < 1 or vehiculo > 3:
                print("Error")
                vehiculo = int(input("¿Qué tipo de vehículo ingresó? 1-Camion 2-Automovil 3-Motocicleta: "))
            matricula = str(input("¿Cual es su matrícula? "))

            hora_entrada = int(input("¿A que hora ingresó el vehículo? "))
            while hora_entrada < 0 or hora_entrada > 22:
                print("Error")
                hora_entrada = int(input("¿A que hora ingresó el vehículo? "))
            
            if vehiculo == 1:
                nuevo_vehiculo = Camion(matricula,hora_entrada)
            elif vehiculo == 2:
                nuevo_vehiculo = Automovil(matricula, hora_entrada)
            elif vehiculo == 3:
                nuevo_vehiculo = Motocicleta(matricula, hora_entrada)            

            registrarDiccionario(vehiculos, nuevo_vehiculo)
            registrarLista(registros, nuevo_vehiculo)
        
        if opciones == 2:
            print("0-Salir")
            for i in range(0,len(registros)):
                print(f"{i+1}- {registros[i].matricula}")
            opcion_salida = int(input("¿Que vehiculo salió? "))
            while opcion_salida < 0 or opcion_salida > len(registros):
                print("Error")
                opcion_salida = int(input("¿Que vehiculo salió? "))

            if opcion_salida != 0:            
                vehiculo_salida = registros[opcion_salida-1]
                hora_salida = int(input("¿A qué hora salio el vehículo? "))
                
                while hora_salida < vehiculo_salida.hora_entrada or hora_salida > 23:
                    print("Error")
                    hora_salida = int(input("¿A qué hora salio el vehículo? "))

                vehiculo_salida.registrar_salida(hora_salida)
                total_ingresos += vehiculo_salida.tarifa_final
                registros.remove(vehiculo_salida)

        elif opciones == 3:
            matricula_info = str(input("Ingrese la matrícula de un vehículo: "))
            if matricula_info in vehiculos:
                print(vehiculos[matricula_info])
            else:
                print("Ningun vehiculo con esa patente pasó por nuestra cochera hoy")
        
        elif opciones == 4:
            salir = True

    print(f"El total de ingresos del dia fue de: ${total_ingresos}")
