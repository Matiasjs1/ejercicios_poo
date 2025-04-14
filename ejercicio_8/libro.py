from datetime import datetime
class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo = titulo
        self.autor = autor
        current_date = datetime.now()
        if anio > current_date.year:
            raise ValueError("No se puede usar un año mayor al actual")
        self.anio = anio
    
    def asignarLibro(self, usuario):
        pass


    def quitarLibro(self, usuario):
        pass

    def mostrarInfo(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"