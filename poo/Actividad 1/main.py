from auto import Auto
from moto import Moto
from persona import Persona

if __name__ == "__main__":
    persona1 = Persona("Renzo", 18, 47350147, True)
    persona1.mostrar_info()
    persona1.puede_conducir()

    persona2 = Persona("Fade", 18, 47812302, False)
    persona2.mostrar_info()
    persona2.puede_conducir()    

    auto1 = Auto("Peugot", 208, 2024, 4)
    auto1.mostrar_info()

    moto1 = Moto("Suzuki", "AX-100", 2024, "98 cc")
    moto1.mostrar_info()