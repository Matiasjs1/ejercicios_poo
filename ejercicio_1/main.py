from persona import Persona
from auto import Auto
from moto import Moto
import os
if __name__ == "__main__":
    persona1 = Persona("Matias",18,47432404, True)
    persona2 = Persona("Jose",19, 45392090, True)
    persona3 = Persona("Juan",20, 45098678, False)

    auto1 = Auto("Toyota", "Corolla", 2022, 4)
    auto2 = Auto("Ford", "Mustang", 2021, 2)
    auto3 = Auto("Chevrolet", "Onix", 2023, 4)

    moto1 = Moto("Yamaha", "YZF-R3", 2022, 321)
    moto2 = Moto("Honda", "CB500F", 2021, 471)
    moto3 = Moto("Kawasaki", "Ninja 400", 2023, 399)

    persona1.mostrar_info()
    persona1.puede_conducir()

    persona2.mostrar_info()
    persona2.puede_conducir()

    persona3.mostrar_info()
    persona3.puede_conducir()

    auto1.asignar_conductor(persona1)
    auto2.asignar_conductor(persona2)
    auto3.asignar_conductor(persona3)

    moto1.asignar_conductor(persona1)
    moto2.asignar_conductor(persona2)
    moto3.asignar_conductor(persona3)
    

    
