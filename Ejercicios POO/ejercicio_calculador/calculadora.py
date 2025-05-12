class Calculadora:
    def __init__(self, precio, descuento):
        self.set_precio(precio)
        self.set_descuento(descuento)


    def set_precio(self, precio):
        
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número")
        self.precio = precio
    
    def set_descuento(self, descuento):
        if not isinstance(descuento, (int, float)):
            raise TypeError("El descuento debe ser un entero")
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        self.descuento = descuento
        
    def calcular_precio_final(self):
        return self.precio - (self.precio * self.descuento / 100)
