from automovil import Automovil
import os

if __name__ == "__main__":
    auto1 = Automovil("Toyota", "Corolla", 2023, "WXZ789", "Marcos", 47490497)
    auto1.mostra_info()
    auto1.mostra_info_dueno()
    print(f"Patente: {auto1.get_patente()}")
    auto1.arrancar()