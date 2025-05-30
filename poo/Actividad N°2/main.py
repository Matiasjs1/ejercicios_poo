from vehiculo import Vehiculo
from moto import Moto
from automovil import Automovil
from camion import Camion

if __name__ == "__main__":
    moto1 = Moto("ABC123", 15)
    camion1 = Camion("CBA123", 12)
    automovil1 = Automovil("ABD321", 10)

    moto1.registrar_informacion()
    camion1.registrar_informacion()
    automovil1.registrar_informacion()

    moto1.calcular_tarifa("Moto", 13, 15)