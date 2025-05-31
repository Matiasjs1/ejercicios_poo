from personaje import Personaje
import random
class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.defensa = 2
        self.ataque = 8    

    def atacar(self):
        porcentaje = random.randint(0,100)
        danio = self.ataque + (self.ataque*porcentaje/100)
        return danio
    
    def defenderse(self, danio):
        danio_recibido = danio - self.defensa
        if danio_recibido < 0:
            danio_recibido = 0
        self.vida -= danio_recibido
        if self.vida < 0:
            self.vida = 0
        return self.vida

    
#<>