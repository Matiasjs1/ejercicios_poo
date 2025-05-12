from curso import Curso
class Curso_presencial(Curso):
    def __init__(self,nombre,codigo,profesor):
        super().__init__(nombre,codigo,profesor)
        self.tipo = "Presencial"

    def calcular_interaccion(self):
        return "Alta"