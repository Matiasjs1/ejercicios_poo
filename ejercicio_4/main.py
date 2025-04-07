from curso_presencial import Curso_presencial
from curso_virtual import Curso_virtual
from curso_grabado import Curso_grabado
from estudiante import Estudiante

if __name__ == "__main__":
    seguir = True
    cursos = {}
    estudiantes = []

    curso_grabado1 = Curso_grabado("Curso de Python", "ABC", "Alan Uzal")
    curso_presencial1 = Curso_presencial("Curso de Java", "POU", "Maria Fava")
    curso_virtual1 = Curso_virtual("Curso de Redes", "ARP", "Matias Maciejewski")

    cursos['ABC'] = curso_grabado1
    cursos['POU'] = curso_presencial1
    cursos['ARP'] = curso_virtual1

    # El programa debe permitir registrar nuevos cursos, inscribir estudiantes a un
    # curso determinado (agregando la tupla del estudiante a la lista) y mostrar
    # un resumen con el nombre del curso, la cantidad de estudiantes y el nivel 
    # de interacción calculado.
    while seguir:
        opcion = int(input("¿Qué desea realizar?: \n1-Registrar nuevos cursos \n2-Inscribir un estudiantes a un curso \n3-Mostrar resumen de curso \n4-Calcular nivel de interacción \n5-Salir\n"))
        while opcion < 1 or opcion > 6:
            print("Error")
            opcion = int(input("¿Qué desea realizar?: \n1-Registrar nuevos cursos \n2-Inscribir un estudiantes a un curso \n3-Mostrar resumen de curso \n4-Calcular nivel de interacción \n5-Salir\n"))
        if opcion == 1:
            nombre = str(input("Escriba el nombre del curso: "))
            tipo = int(input("Qué tipo de curso es: 1-Presencial, 2-Virtual, 3-Grabado "))
            while tipo < 1 or tipo > 3:
                print("Error")
                tipo = int(input("Qué tipo de curso es: 1-Presencial, 2-Virtual, 3-Grabado "))
            codigo = str(input("Escriba el codigo del curso: "))
            profesor = str(input("Escriba el nombre del profesor del curso: "))
            if codigo not in cursos:
                if tipo == 1:
                    curso_creado = Curso_presencial()
                elif tipo == 2:
                    curso_creado = Curso_virtual()
                elif tipo == 3:
                    curso_creado = Curso_grabado()

                cursos[codigo] = curso_creado
            else:
                print("Ya existe un curso con dicho código")
        
        elif opcion == 2:
            pass




        elif opcion == 5:
            seguir = False