from curso import Curso
class Curso_grabado(Curso):
    def __init__(self,nombre,codigo,profesor):
        super().__init__(nombre,codigo,profesor)
        self.tipo = "Grabado"

    def calcular_interaccion(self):
        valor_base = 40
        valor_alumnos = len(self.__estudiantes)
        valor_total = valor_base + valor_alumnos
        if valor_total >= 70:
            return "Media"
        elif valor_total >= 100:
            return "Alta"
        else:
            return "Baja"