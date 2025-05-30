class Vehiculo:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.__dni = dni
    
    def get_dni(self):
        return self.__dni
    
    def set_dni(self, dni):
        self.__dni = dni
    
    def mostra_info_dueno(self):
        print(f"Datos dueño: {self.nombre}, {self.get_dni()}")