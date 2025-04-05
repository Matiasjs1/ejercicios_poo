from personaje import Personaje
class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.defensa += 0.05*self.defensa
        self.ataque -= 3
        