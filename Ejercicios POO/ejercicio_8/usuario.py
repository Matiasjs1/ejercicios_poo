import os
class Usuario:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.__dni = dni
        self.libros = []

    def pedirLibro(self, libro):
        if len(self.libros) >= 3:
            raise ValueError("No se pueden pedir más de 3 libros")
        try:
            libro.asignarLibro(self)
        except ValueError as e:
            os.system("cls")
            print("Error: ", e)
            os.system("pause")


    def devolverLibro(self, libro):
        try:
            libro.quitarLibro(self)
        except ValueError as e:
            os.system("cls")
            print("Error: ", e)
            os.system("pause")