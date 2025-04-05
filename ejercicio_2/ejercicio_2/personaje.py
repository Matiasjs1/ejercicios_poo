from item import Item
class Personaje:
    def __init__(self,nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 7
        self.defensa = 3
        self.inventario = []

    def recibir_danio(self, danio):
        self.vida -= danio
        if self.vida < 0:
            self.vida = 0
            
    def atacar(self, otro_personaje):
        danio = self.ataque - otro_personaje.defensa
        otro_personaje.recibir_danio(danio)



    def agregar_item(self, item):
        self.inventario.append(item)

    def mostrarStats(self):
        print(f"""{self.nombre}:
Vida:{self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
              """)