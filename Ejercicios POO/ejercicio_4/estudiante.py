class Estudiante:
    def __init__(self, nombre, dni, correo):
        self.nombre = nombre
        self.__dni = dni
        self.correo = correo

    