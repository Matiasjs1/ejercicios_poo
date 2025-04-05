class Item:
    def __init__(self, nombre, tipo, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
    
    def usar(self, personaje):
        if self.tipo == "pocion":
            personaje.vida += self.valor
        elif self.tipo == "arma":
            personaje.ataque += self.valor
        elif self.tipo == "escudo":
            personaje.defensa += self.valor
