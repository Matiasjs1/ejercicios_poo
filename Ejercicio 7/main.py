from agenciaInmobiliaria import AgenciaInmobiliaria
import os
if __name__ == "__main__":
    seguir = True
    agencia = AgenciaInmobiliaria()
    while seguir:
        os.system("cls")
        opcion = int(input("Seleccione una opción:\n1-Agregar Propiedad\n2-Agregar Cliente\n3-Buscar Propiedad por ID\n4-Listar propiedades disponibles\n5-Filtrar por zona\n6-Propiedad más cara\n7-Promedio Precios\n8-Clientes interesados en la propiedad\n9-Reporte General\n10-Salir\n"))
        while opcion < 1 or opcion > 10:
            print("Error")
            opcion = int(input("Seleccione una opción:\n1-Agregar Propiedad\n2-Agregar Cliente\n3-Buscar Propiedad por ID\n4-Listar propiedades disponibles\n5-Filtrar por zona\n6-Propiedad más cara\n7-Promedio Precios\n8-Clientes interesados en la propiedad\n9-Reporte General\n10-Salir\n"))
        
        if opcion == 1:
            os.system("cls")
            agencia.agregar_propiedad()
            os.system("pause")

        elif opcion == 2:
            os.system("cls")
            agencia.agregar_cliente()
            os.system("pause")

        elif opcion == 3:
            os.system("cls")
            agencia.buscar_propiedad_por_id()
            os.system("pause")

        elif opcion == 4:
            os.system("cls")
            agencia.listar_disponibles()
            os.system("pause")

        elif opcion == 5:
            os.system("cls")
            agencia.filtrar_por_zona()
            os.system("pause")

        elif opcion == 6:
            os.system("cls")
            agencia.propiedad_mas_cara()
            os.system("pause")
        
        elif opcion == 7:
            os.system("cls")
            tipoElegido = int(input("¿De qué tipo de propiedad quiere sacar un promedio de precios? 1-Alquiler 2-Venta: "))
            while tipoElegido != 1 and tipoElegido != 2:
                print("Error")
                tipoElegido = int(input("¿De qué tipo de propiedad quiere sacar un promedio de precios? 1-Alquiler 2-Venta: "))
            if tipoElegido == 1:
                tipo = "Alquiler"
            elif tipoElegido == 2:
                tipo = "Venta"
            agencia.promedio_precios(tipo)
            os.system("pause")

        elif opcion == 8:
            os.system("cls")
            propiedad = None
            id_elegida = int(input("Seleccione la ID de la propiedad que quiere buscar si tiene clientes interesados: "))
            for i in agencia.propiedades:
                if i.id_propiedad == id_elegida:
                    propiedad = i
            if propiedad == None:
                print("No se encontró dicha propiedad")
            else:
                agencia.clientes_interesados_en(propiedad)
            os.system("pause")

        
        elif opcion == 9:
            os.system("cls")
            agencia.reporte_general()
            os.system("pause")

        elif opcion == 10:
            os.system("cls")
            print("Se terminará el programa")
            os.system("pause")
            seguir = False