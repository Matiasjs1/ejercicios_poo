from agenciaMarkting import AgenciaMarketing
import os
from campaniaRedesSociales import CampaniaRedesSociales
from campaniaSEO import CampaniaSEO
if __name__ == "__main__":
    agencia = AgenciaMarketing()
    seguir = True
    while seguir:
        os.system("cls")
        opciones = int(input("Seleccione una opcion:\n1-Agregar Campania\n2-Listar campania por tipo\n3-Ranking eficiencia\n4-Cliente con más ROI\n5-Campaña con más eficiencia\n6-Informe de cliente\n7-Salir\n"))
        while opciones > 7 or opciones < 1:
            os.system("cls")
            print("Error")
            opciones = int(input("Seleccione una opcion:\n1-Agregar Campania\n2-Listar campania por tipo\n3-Ranking eficiencia\n4-Cliente con más ROI\n5-Campaña con más eficiencia\n6-Informe de cliente\n7-Salir\n"))


        if opciones == 1:
            cliente = str(input("Ingrese el nombre del cliente: "))
            presupuesto = float(input("Ingrese el presupuesto (en U$D): "))
            while presupuesto < 0:
                print("Valor incorrecto")
                presupuesto = float(input("Ingrese el presupuesto (en U$D): "))
            duracion = int(input("Ingrese la duración (en días): "))
            while duracion < 0:
                print("Valor incorrecto")
                duracion = int(input("Ingrese la duración (en días): "))
            tipoElegido = int(input("Seleccione el tipo de campaña: 1-Redes Sociales 2-SEO: "))
            while tipoElegido > 2 or tipoElegido < 1:
                print("Valor incorrecto")
                tipoElegido = int(input("Seleccione el tipo de campaña: 1-Redes Sociales 2-SEO: "))
            if tipoElegido == 1:
                tipo = "CampaniaRedesSociales"
            elif tipoElegido == 2:
                tipo = "CampaniaSEO"
            agencia.agregarCampania(cliente, presupuesto, duracion, tipo)
            print("Se agregó la nueva campaña")
            os.system("pause")
        
        elif opciones == 2:
            tipoElegido = int(input("Seleccione el tipo de campaña a listar: 1-Redes Sociales 2-SEO: "))
            while tipoElegido > 2 or tipoElegido < 1:
                print("Valor incorrecto")
                tipoElegido = int(input("Seleccione el tipo de campaña: 1-Redes Sociales 2-SEO: "))
            if tipoElegido == 1:
                tipo = CampaniaRedesSociales
            elif tipoElegido == 2:
                tipo = CampaniaSEO
            lista = agencia.listarCampania(tipo)
            if len(lista) == 0:
                print("No hay agencias en esta categoría")
            else:
                for i in lista:
                    i.mostrar_info()
                os.system("pause")
        
        elif opciones == 3:
            ranking = agencia.calcularRanking()
            for i in ranking:
                i.mostrar_info()
            os.system("pause")
        
        elif opciones == 4:
            clienteMayor = agencia.calcularClienteMasROI()
            os.system("pause")

        elif opciones == 5:
            campania = agencia.campaniaMayorEficiencia()
            os.system("pause")

        elif opciones == 6:
            clienteAnalizar = str(input("Ingrese el nombre del cliente a analizar: "))
            agencia.mostrar_informe_general(clienteAnalizar)
            os.system("pause")

        elif opciones == 7:
            seguir = False