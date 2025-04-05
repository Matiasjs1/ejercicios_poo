"""

Cada vehículo tendrá un número de matrícula único, el tipo de vehículo
(automóvil, motocicleta o camión), la hora de entrada y la hora de salida.
Cuando un vehículo entra en el estacionamiento, se registra su información en
una lista de vehículos en circulación, utilizando un diccionario donde la
clave es la matrícula y el valor es una tupla con los datos del vehículo.
Al momento de salir, se calcula la tarifa en función del tipo de vehículo
y el tiempo que ha permanecido en el estacionamiento. Los automóviles
tienen una tarifa base de 10 unidades por hora, las motocicletas pagan un
20% menos que los automóviles y los camiones un 50% más.

"""

class Vehiculo:
    def __init__(self, matricula, hora_entrada):
        self.matricula = matricula
        self.hora_entrada = hora_entrada
        self.hora_salida = None
        self.tarifa_final = None
        self.tipo = None
        self.datos = self.matricula, self.hora_entrada, self.tipo
    
    def registrar_salida(self, hora_salida):
        if hora_salida < self.hora_entrada or hora_salida > 23:
            print("Error. Valor invalido")
            return False
        else:
            self.hora_salida = hora_salida
            self.calcular_tarifa()
            print(f"Salio un vehiculo. Tarifa del vehiculo: {self.tarifa_final}")
            return True
    
    def calcular_tarifa(self):
        pass

