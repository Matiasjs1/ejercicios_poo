from libro import Libro
from datetime import datetime
class LibroFisico(Libro):
    def __init__(self, titulo, autor, anio, disponibilidad):
        super().__init__(titulo, autor, anio)
        self.disponibilidad = disponibilidad


    def asignarLibro(self, usuario):
        if self.disponibilidad == False:
            raise ValueError("El libro no esta disponible")
        usuario.libros.append((self, datetime.now()))
        self.disponibilidad = False

    
    def quitarLibro(self, usuario):
        tupla = None
        for libro, fecha in usuario.libros:
            if libro == self:
                tupla = (libro, fecha)
        if tupla == None:
            raise ValueError("El usuario no tiene ese libro")
        diferencia = datetime.now() - tupla[1]
        if diferencia.days > 30:
            raise ValueError("No se puede tardar más de 30 dias en devolver un libro")
        usuario.libros.remove(tupla)
        self.disponibilidad = True

    def mostrarInfo(self):
        devolver = super().mostrarInfo()
        devolver += f"Disponibilidad: {self.disponibilidad}"
        return devolver
