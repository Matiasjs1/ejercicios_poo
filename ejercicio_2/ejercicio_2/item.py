class Item:
    def __init__(self,nombre,tipo,valor):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
    
    def usar(self, personaje):
        if self.tipo == "pocion":
            personaje.vida += self.valor
            personaje.inventario.remove(self)
        elif self.tipo == "arma":
            personaje.ataque += self.valor
            personaje.inventario.remove(self)
        elif self.tipo == "escudo":
            personaje.defensa += self.valor
            personaje.inventario.remove(self)
    
    