from personaje import Personaje
class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ataque += 0.07*self.ataque
        self.defensa -= 5
        