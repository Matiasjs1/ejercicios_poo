from libroDigital import LibroDigital
from libroFisico import LibroFisico
from usuario import Usuario
import datetime
import os

if __name__ == "__main__":
    diccionarioLibros = {}
    listaPrestamos = []

    libro_digital_1 = LibroDigital("El código Da Vinci", "Dan Brown", 2003, "PDF")
    libro_digital_2 = LibroDigital("1984", "George Orwell", 1949, "EPUB")
    libro_digital_3 = LibroDigital("Cien años de soledad", "Gabriel García Márquez", 1967, "MOBI")
    libro_digital_4 = LibroDigital("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "PDF")
    libro_digital_5 = LibroDigital("El gran Gatsby", "F. Scott Fitzgerald", 1925, "EPUB")
    libro_digital_6 = LibroDigital("La sombra del viento", "Carlos Ruiz Zafón", 2001, "MOBI")
    libro_digital_7 = LibroDigital("Matar a un ruiseñor", "Harper Lee", 1960, "PDF")
    libro_digital_8 = LibroDigital("El principito", "Antoine de Saint-Exupéry", 1943, "EPUB")
    libro_digital_9 = LibroDigital("Orgullo y prejuicio", "Jane Austen", 1813, "MOBI")
    libro_digital_10 = LibroDigital("Crimen y castigo", "Fiódor Dostoyevski", 1866, "PDF")

    libro_fisico_1 = LibroFisico("El alquimista", "Paulo Coelho", 1988, True)
    libro_fisico_2 = LibroFisico("Los pilares de la Tierra", "Ken Follett", 1989, True)
    libro_fisico_3 = LibroFisico("El nombre de la rosa", "Umberto Eco", 1980, True)
    libro_fisico_4 = LibroFisico("El retrato de Dorian Gray", "Oscar Wilde", 1890, True)
    libro_fisico_5 = LibroFisico("Fahrenheit 451", "Ray Bradbury", 1953, True)
    libro_fisico_6 = LibroFisico("La metamorfosis", "Franz Kafka", 1915, True)
    libro_fisico_7 = LibroFisico("El viejo y el mar", "Ernest Hemingway", 1952, True)
    libro_fisico_8 = LibroFisico("Cumbres borrascosas", "Emily Brontë", 1847, True)
    libro_fisico_9 = LibroFisico("La tregua", "Mario Benedetti", 1960, True)
    libro_fisico_10 = LibroFisico("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, True)

    diccionarioLibros[libro_digital_1.autor] = libro_digital_1
    diccionarioLibros[libro_digital_2.autor] = libro_digital_2
    diccionarioLibros[libro_digital_3.autor] = libro_digital_3
    diccionarioLibros[libro_digital_4.autor] = libro_digital_4
    diccionarioLibros[libro_digital_5.autor] = libro_digital_5
    diccionarioLibros[libro_digital_6.autor] = libro_digital_6
    diccionarioLibros[libro_digital_7.autor] = libro_digital_7
    diccionarioLibros[libro_digital_8.autor] = libro_digital_8
    diccionarioLibros[libro_digital_9.autor] = libro_digital_9
    diccionarioLibros[libro_digital_10.autor] = libro_digital_10

    diccionarioLibros[libro_fisico_1.autor] = libro_fisico_1
    diccionarioLibros[libro_fisico_2.autor] = libro_fisico_2
    diccionarioLibros[libro_fisico_3.autor] = libro_fisico_3
    diccionarioLibros[libro_fisico_4.autor] = libro_fisico_4
    diccionarioLibros[libro_fisico_5.autor] = libro_fisico_5
    diccionarioLibros[libro_fisico_6.autor] = libro_fisico_6
    diccionarioLibros[libro_fisico_7.autor] = libro_fisico_7
    diccionarioLibros[libro_fisico_8.autor] = libro_fisico_8
    diccionarioLibros[libro_fisico_9.autor] = libro_fisico_9
    diccionarioLibros[libro_fisico_10.autor] = libro_fisico_10

    listaUsuarios = [
        Usuario("Juan Pérez", "12345678"),
        Usuario("Ana Gómez", "23456789"),
        Usuario("Carlos López", "34567890"),
        Usuario("María Sánchez", "45678901"),
        Usuario("Pedro Martínez", "56789012"),
        Usuario("Laura Rodríguez", "67890123"),
        Usuario("Luis Fernández", "78901234"),
        Usuario("Elena García", "89012345"),
        Usuario("Antonio Díaz", "90123456"),
        Usuario("Marta Romero", "01234567")
    ]

    salir = False
    while not salir:
        
        try:
            os.system("cls")
            accion = int(input("Que desea hacer? 1- Sacar libro, 2- Devolver libro 3- Salir: "))
            if accion < 1 or accion > 3:
                raise ValueError("Elegi un valor del 1 al 3")
        except Exception as e:
            os.system("cls")
            print("Error: ", e)
            os.system("pause")
            continue
        
        if accion == 1:
            os.system("cls")
            valor = 0
            for i in listaUsuarios:
                valor += 1
                print(f"{valor}- {i.nombre}")
            
            try:
                valorIngresado = int(input("Que usuario desea retirar un libro? "))
                if valorIngresado < 1 or valorIngresado > len(listaUsuarios):
                    raise ValueError("El usuario no se encuentra en la lista")
            except ValueError as e:
                os.system("cls")
                print("Error: ",e)
                os.system("pause")
                continue
            
            usuario = listaUsuarios[valorIngresado-1]

            valor = 0
            for i in diccionarioLibros.values():
                valor += 1
                print(f"{valor}- {i.mostrarInfo()}")
            try:
                autorElegido = str(input("Seleccione el autor del libro que desea reservar: "))
                if autorElegido not in diccionarioLibros:
                    raise ValueError("El valor ingresado no estaba en las opciones")
            except ValueError as e:
                os.system("cls")
                print("Error: ", e)
                os.system("pause")
                continue
            libro = diccionarioLibros[autorElegido]
            usuario.pedirLibro(libro)

        elif accion == 2:
            os.system("cls")
            valor = 0
            for i in listaUsuarios:
                valor += 1
                print(f"{valor}- {i.nombre}")
            
            try:
                valorIngresado = int(input("Que usuario desea retirar un libro? "))
                if valorIngresado < 1 or valorIngresado > len(listaUsuarios):
                    raise ValueError("El usuario no se encuentra en la lista")
                if len(listaUsuarios[valorIngresado-1].libros) == 0:
                    raise ValueError("El usuario no tiene libros")
            except ValueError as e:
                os.system("cls")
                print("Error: ",e)
                os.system("pause")
                continue
            
            usuario = listaUsuarios[valorIngresado-1]

            valor = 0
            os.system("cls")
            for i in usuario.libros:
                valor +=1
                print(f"{valor}- {i[0].mostrarInfo()}")
            try:
                libroDevolver = int(input("Seleccione el libro a devolver: "))
                if libroDevolver <1 or libroDevolver > len(usuario.libros):
                    raise ValueError ("El valor ingresado es invalido")
            except ValueError as e:
                os.system("cls")
                print("Error: ", e)
                os.system("pause")
                continue
            usuario.devolverLibro(usuario.libros[libroDevolver-1])
        elif accion == 3:
            salir = True
            

