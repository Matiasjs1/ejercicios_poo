class Curso:
    def __init__(self,nombre,codigo,profesor):
        self.nombre = nombre
        self.__codigo = codigo
        self.profesor = profesor
        self.__estudiantes = []
    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} \n Profesor: {self.profesor} \n Cantidad de alumnos: {len(self.__estudiantes)}")

    def calcular_interaccion(self):
        pass
