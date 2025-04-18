from propiedadAlquiler import PropiedadAlquiler
from propiedadVenta import PropiedadVenta
class Cliente:
    def __init__(self, nombre, dni, email, zona, ambientes, tipo):
        self.nombre = nombre
        self.__dni = dni
        self.email = email
        self.preferencias = {"Zona":zona, "Ambientes":ambientes, "Tipo":tipo}

    def getDni(self):
        return self.__dni
    
    def setDni(self, dni):
        self.__dni = dni

    def mostrarPreferencias(self):
        print(f"Preferencias del cliente: {self.nombre}")
        for x, y in self.preferencias.items:
            print(x, y)
    
    def coincidencias(self, lista):
        listaCoincidencias = []
        for i in lista:
            if type(i) == PropiedadVenta:
                tipo = "Venta"
            elif type(i) == PropiedadAlquiler:
                tipo = "Alquiler"
            if i.zona == self.preferencias["Zona"] and i.ambientes == self.preferencias["Ambientes"] and tipo == self.preferencias["Tipo"]:
                listaCoincidencias.append(i)

        return listaCoincidencias