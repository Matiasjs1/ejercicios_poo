class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 7
        self.defensa  = 3
        self.inventario = []
    
    def atacar(self, otro_personaje):
        danio_total = (self.ataque - otro_personaje.defensa)
        if danio_total < 0:
            danio_total = 0
        otro_personaje.vida -= danio_total
        if otro_personaje.vida < 0:
            otro_personaje.vida = 0

    def recibir_danio(self, danio):
        danio_total = (danio - self.defensa)
        if danio_total < 0:
            danio_total = 0
        self.vida -= danio_total
        if self.vida < 0:
            self.vida = 0

    def agregar_item(self, item):
        self.inventario.append(item)