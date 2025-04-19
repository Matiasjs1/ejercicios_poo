from torneo import Torneo
from boxeadorAmateur import BoxeadorAmateur
from boxeadorProfesional import BoxeadorProfesional
import os


def main():
    torneo = Torneo()
    seguir = True
    while seguir:
        os.system("cls")
        opciones = int(input("Opciones:\n1-Agregar Boxeador\n2-Listar Boxeadores\n3-Calcular promedio de edad por categoria\n4-Boxeador con más puntaje\n5-Ranking Eficiencia\n6-Ranking General\n7-Salir\n"))
        while opciones < 1 or opciones > 7:
            os.system("cls")
            print("Error")
            opciones = int(input("Opciones:\n1-Agregar Boxeador\n2-Listar Boxeadores\n3-Calcular promedio de edad por categoria\n4-Boxeador con más puntaje\n5-Ranking Eficiencia\n6-Ranking General\n7-Salir\n"))

        if opciones == 1:
            os.system("cls")
            nombre = str(input("Ingrese el nombre del boxeador: "))
            dni = int(input("Ingrese el DNI del boxeador: "))
            while dni < 1:
                print("Error")
                dni = int(input("Ingrese el DNI del boxeador: "))
            edad = int(input("Ingrese la edad del boxeador: "))
            while edad < 0:
                print("Error")
                edad = int(input("Ingrese la edad del boxeador: "))
            peso = int(input("Ingrese el peso del boxeador: "))
            while peso < 0:
                print("Error")
                peso = int(input("Ingrese el peso del boxeador: "))
            tipo = int(input("¿El boxeador es amateur o profesional? 1-Amateur 2-Profesional "))
            while tipo < 1 or tipo > 2:
                print("Error")
                tipo = int(input("¿El boxeador es amateur o profesional? 1-Amateur 2-Profesional "))
            if tipo == 1:
                boxeador = BoxeadorAmateur(nombre, dni, edad, peso)
            elif tipo == 2:
                boxeador = BoxeadorProfesional(nombre, dni, edad, peso)

            while True:
                otraPelea = int(input("Desea agregar una pelea: 1-Si 2-No: "))
                while otraPelea < 1 or otraPelea > 2:
                    print("Error")
                    otraPelea = int(input("Desea agregar una pelea: 1-Si 2-No: "))
                if otraPelea == 1:
                    oponente = str(input("Ingrese el nombre del oponente: "))
                    resultado = int(input("¿Cómo salio la pelea?: 1-Victoria 2-Empate 3-Derrota "))
                    while resultado < 1 or resultado > 3:
                        print("Error")
                        resultado = int(input("¿Cómo salio la pelea?: 1-Victoria 2-Empate 3-Derrota "))
                    puntaje = int(input("Ingrese el puntaje obtenido en la pelea: "))
                    while puntaje < 0:
                        print("Error")
                        puntaje = int(input("Ingrese el puntaje obtenido en la pelea: "))
                    boxeador.historial.append((oponente, resultado, puntaje))
                
                elif otraPelea == 2:
                    break
            torneo.agregarBoxeador(boxeador)
            print("Se agregó un boxeador")
            os.system("pause")
        
        elif opciones == 2:
            os.system("cls")
            categoriaElegida = str(input("Ingrese la categoria a listar: "))
            lista = torneo.listarBoxeador(categoriaElegida)
            if len(lista) == 0:
                print("No se ingresaron boxeadores")
            else:
                for i in lista:
                    i.mostrar_info()
            os.system("pause")
        
        elif opciones == 3:
            os.system("cls")
            categoriaElegida = str(input("Ingrese la categoria para sacar promedio: "))
            print(torneo.calcularPromedioEdadCategoria(categoriaElegida))
            os.system("pause")
            
        elif opciones == 4:
            os.system("cls")
            boxeador = torneo.boxeadorMasPuntaje()
            print("El boxeador con más puntaje es: ")
            boxeador.mostrar_info()
            os.system("pause")

        elif opciones == 5:
            os.system("cls")
            lista = torneo.rankingEficiencia()
            for i in lista:
                i[0].mostrar_info()
            os.system("pause")

        elif opciones == 6:
            os.system("cls")
            lista = torneo.rankingGeneral()
            for i in lista:
                i[0].mostrar_info()
            os.system("pause")

        elif opciones == 7:
            seguir = False


if __name__ == "__main__":
    main()
# <>