class ErrorEspecialidad(Exception):
    def __init__(self, mensaje = "No se encuentran las 3 especialidades básicas"):
        super().__init__(mensaje)