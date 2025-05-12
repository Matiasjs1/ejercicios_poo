class ValoresNegativos(Exception):
    def __init__(self, mensaje="Se ingreso un valor negativo en la velocidad"):
        super().__init__(mensaje)

class ValoresFueraRango(Exception):
    def __init__(self, mensaje="Se ingreso un valor fuera de rango en la intensidad"):
        super().__init__(mensaje)
