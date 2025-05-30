from personaje import Personaje

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ataque *= 1.07
        self.defensa -= 5