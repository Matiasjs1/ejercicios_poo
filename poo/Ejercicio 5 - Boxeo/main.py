from boxeador import Boxeador
from boxeadorAmateur import BoxeadorAmateur
from boxeadorProfesional import BoxeadorProfesional
from torneo import Torneo

def main():
    torneo = Torneo()
    seguir = True
    while seguir == True:
        while True:
            try:
                opciones = int(input("Opciones:\n1-Agregar Boxeador\n2-Listar Boxeadores\n3-Calcular promedio de edad por categoria\n4-Boxeador con más puntaje\n5-Ranking Eficiencia\n6-Ranking General\n7-Salir\n"))
                if opciones < 1 or opciones > 7:
                    raise ValueError("Valor fuera de rango")
                break
            except ValueError as e:
                print("Error: ", e)

        if opciones == 1:
            while True:
                try:
                    tipoBoxeador = int(input("Que tipo de boxeador es? 1- Amateur, 2- Profesional"))
                    if tipoBoxeador < 1 or tipoBoxeador > 2:
                        raise ValueError("Valor fuera de rango")
                    break
                except ValueError as e:
                    print("Error: ", e)
            
            try:
                nombreBoxeador = str(input("Nombre: "))
                dniBoxeador = int(input("Dni: "))
                edadBoxeador = int("Edad: ")
                pesoBoxeador = float("Peso: ")
                if tipoBoxeador == 1:
                    boxeadorNuevo = BoxeadorAmateur(nombreBoxeador, dniBoxeador, edadBoxeador, pesoBoxeador)
                elif tipoBoxeador == 2:
                    boxeadorNuevo = BoxeadorProfesional(nombreBoxeador, dniBoxeador, edadBoxeador, pesoBoxeador)
                torneo.agregarBoxeadores(boxeadorNuevo)
            except ValueError as e:
                print("Error: ", e)
            
            agregarOtraPelea = 1
            while agregarOtraPelea == 1:
                while True:
                    try:
                        agregarOtraPelea = int(input("Desea ingresar una pelea? 1- Si, 2- No"))
                        if agregarOtraPelea < 1 or agregarOtraPelea > 2:
                            raise ValueError("Valor fuera de rango")
                        
                        if agregarOtraPelea == 1:
                            oponente = str(input("Nombre del oponente: "))
                            resultado = int(input("Resultado? 1- Victoria, 2- Empate, 3- Derrota"))
                            if resultado < 1 or resultado > 3:
                                raise ValueError("Valor fuera de rango")
                            puntaje = float(input("Puntos ganados: "))
                            if puntaje < 1:
                                raise ValueError("No se puede ganar menos de 1 punto")

                            if resultado == 1:
                                boxeadorNuevo.historial.append((oponente, "Victoria", puntaje))
                            elif resultado == 2:
                                boxeadorNuevo.historial.append((oponente, "Empate", puntaje))
                            elif resultado == 3:
                                boxeadorNuevo.historial.append((oponente, "Derrota", puntaje))
                        
                        elif agregarOtraPelea == 2:
                            agregarOtraPelea = 2
                        break

                    except ValueError as e:
                        print("Error: ", e)
                

        elif opciones == 2:
            while True:
                try:
                    categoriaAListar = int(input("Que categoria desea listar? 1- Liviano, 2- Mediano, 3- Pesado"))
                    if categoriaAListar < 1 or categoriaAListar > 3:
                        raise ValueError("Valor fuera de rango")
                    break
                except ValueError as e:
                    print("Error: ", e)
            if categoriaAListar == 1:
                torneo.listarCategoria("Liviano")
            elif categoriaAListar == 2:
                torneo.listarCategoria("Mediano")
            elif categoriaAListar == 3:
                torneo.listarCategoria("Pesado")

if __name__ == "__main__":
    main()