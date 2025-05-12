class Vehiculo:
    def __init__(self, matricula, hora_entrada):
        self.matricula = matricula
        self.hora_entrada = hora_entrada
        self.tarifa = 10
        self.hora_salida = None
    
    def registrar_informacion(self):
        print(f"{self.tipo}, {self.matricula}, {self.hora_entrada}")

    def calcular_tarifa(self, tipo, hora_entrada, hora_salida):
        hora = hora_salida - hora_entrada
        if tipo == "Automovil":
            self.tarifa = self.tarifa * hora
        elif tipo == "Moto":
            self.tarifa = self.tarifa - (self.tarifa * hora) * 0.2
        elif tipo == "Camion":
            self.tarifa = self.tarifa - (self.tarifa * hora) * 1.5
        print(f"Tarifa: {self.tarifa}")

    
