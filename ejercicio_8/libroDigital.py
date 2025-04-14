from libro import Libro
from datetime import datetime
class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato):
        super().__init__(titulo, autor, anio)
        self.formato = formato

    def asignarLibro(self, usuario):
        usuario.libros.append((self, datetime.now()))
    
    def quitarLibro(self, usuario):
        tupla = None
        for libro, fecha in usuario.libros:
            if libro == self:
                tupla = (libro, fecha)
        if tupla == None:
            raise ValueError("El usuario no tiene ese libro")
        diferencia = datetime.now() - tupla[1]
        if diferencia.day() > 30:
            raise ValueError("No se puede tardar más de 30 dias en devolver un libro")
        usuario.libros.remove(tupla)

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Formato: {self.formato}")