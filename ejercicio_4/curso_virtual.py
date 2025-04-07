from curso import Curso
class Curso_virtual(Curso):
    def __init__(self,nombre,codigo,profesor):
        super().__init__(nombre,codigo,profesor)
        self.tipo = "Virtual"

    def calcular_interaccion(self):
        valor_base = 70
        valor_alumnos = len(self.__estudiantes)
        valor_total = valor_base + valor_alumnos
        if valor_total >= 100:
            return "Alta"
        else:
            return "Media"