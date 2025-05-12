from automovil import Automovil
import os

if __name__ == "__main__":
    auto1 = Automovil("Toyota", "Corolla", 2023, "A58S6","Matias",47432404)
    auto1.mostra_info()
    auto1.mostrar_info_duenio()
    print(f"Patente: {auto1.get_patente()}")
    auto1.arrancar()