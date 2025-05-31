from persona import Persona
from moto import Moto
from auto import Auto
import os

def asignarConductor(vehiculo):
    if vehiculo.conductor != None:
        print("El vehiculo ya tiene conductor")
    else:
        conductorElegido = int(input(f"Seleccione un conductor para el vehiculo: 1-{persona1.nombre}, 2-{persona2.nombre}, 3-{persona3.nombre}, 4-{persona4.nombre} "))
        while conductorElegido > 4 or conductorElegido < 1:
            conductorElegido = int(input(f"Seleccione un conductor para el vehiculo: 1-{persona1.nombre}, 2-{persona2.nombre}, 3-{persona3.nombre}, 4-{persona4.nombre} "))             
        if conductorElegido == 1:
            if persona1.licencia_conducir == None:
                print("El conductor no tiene licencia de conducir")
            else:
                vehiculo.asignar_conductor(persona1)
                print("Se ha asignado el conductor para el vehiculo")

        elif conductorElegido == 2:
            if persona2.licencia_conducir == None:
                print("El conductor no tiene licencia de conducir")
            else:
                vehiculo.asignar_conductor(persona2)
                print("Se ha asignado el conductor para el vehiculo")

        elif conductorElegido == 3:
            if persona3.licencia_conducir == None:
                print("El conductor no tiene licencia de conducir")
            else:
                vehiculo.asignar_conductor(persona3)
                print("Se ha asignado el conductor para el vehiculo")
                    
        elif conductorElegido == 4:
            if persona4.licencia_conducir == None:
                print("El conductor no tiene licencia de conducir")
            else:
                vehiculo.asignar_conductor(persona4)
                print("Se ha asignado el conductor para el vehiculo")

if __name__ == "__main__":
    persona1 = Persona("Juan Pérez", 30, "34381239")
    persona2 = Persona("María Gómez", 25, "32833210")
    persona3 = Persona("Carlos López", 40, "36940023")
    persona4 = Persona("Juan Fernando Quintero", 32, "35271929")
    
    persona1.puede_conducir()
    persona2.puede_conducir()
    persona4.puede_conducir()

    moto1 = Moto("BMW", "R 1250 GS", "2020", "1200cc")
    moto2 = Moto("Honda", "Fireblade", "2024", "1000")
    auto1 = Auto("Chevrolet", "Camaro" , "2024", 2)
    auto2 = Auto("Toyota", "Corolla", "2024", 4)

    salir = False
    
    while salir == False:
        opcion = int(input("Seleccionar una opcion: 1-Ver informacion Autos 2-Asignar conductores 3-Salir: "))
        while opcion != 1 and opcion != 2 and opcion != 3:
                os.system('cls')
                print("Error")
                opcion = int(input("Seleccionar una opcion: 1-Ver informacion de vehículos 2-Asignar conductores 3-Salir: "))
              
        if opcion == 1:
            moto1.mostrar_info()
            moto2.mostrar_info()
            auto1.mostrar_info()
            auto2.mostrar_info()
            os.system("pause")
            os.system("cls")

        elif opcion == 2:
            print(f"Seleccione un vehiculo: 1-{moto1.marca} {moto1.modelo}, 2-{moto2.marca} {moto2.modelo}, 3-{auto1.marca} {auto1.modelo}, 4-{auto2.marca} {auto2.modelo} ")
            opcionVehiculo = int(input())
            while opcionVehiculo > 4 or opcionVehiculo < 1:
                os.system('cls')
                print("Error")
                print(f"Seleccione un vehiculo: 1-{moto1.marca} {moto1.modelo}, 2-{moto2.marca} {moto2.modelo}, 3-{auto1.marca} {auto1.modelo}, 4-{auto2.marca} {auto2.modelo} ")
                opcionVehiculo = int(input())
            os.system('cls')

            if opcionVehiculo == 1:
                asignarConductor(moto1)
            if opcionVehiculo == 2:
                asignarConductor(moto2)
            if opcionVehiculo == 3:
                asignarConductor(auto1)
            if opcionVehiculo == 4:
                asignarConductor(auto2)
        
        if opcion == 3:
            salir == True
            exit()        