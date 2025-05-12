class Astronauta:
    def __init__(self,nombre,edad,especialidad):
        
        self.setEdad(edad)
        self.nombre = nombre
        self.especialidad = especialidad
        self.salud = 100

    def setEdad(self,edad):
        if edad < 0:
            raise ValueError("No puede existir una edad menor a 0")
        self.edad = edad

    def recibirDanio(self, danio):
        self.salud -= danio
        if self.salud <= 0:
            self.salud = 0
            print(f"Murio el astronauta {self.nombre}")



# nombre, edad, una especialidad (como navegación, medicina
# o mantenimiento) y un nivel de salud 