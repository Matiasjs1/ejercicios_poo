import os
from agenciaInmobiliaria import AgenciaInmobiliaria
from propiedadAlquiler import PropiedadAlquiler
from propiedadVenta import PropiedadVenta
from cliente import Cliente


def main():
    agenciaInmobiliaria = AgenciaInmobiliaria()
    while True:
        opcion = int(input("Elija: 1-Gestionar propiedades en venta y en alquiler 2-Registrar clientes interesados 3-Analizar datos: "))
        while opcion < 1 and opcion > 3:
            print("ERROR")
            opcion = int(input("Elija: 1-Gestionar propiedades en venta y en alquiler 2-Registrar clientes interesados 3-Analizar datos: "))
        if opcion == 1:
            opcion1 = int(input("Elija: 1-Ingresar propiedad 2-Vender/Alquilar propiedad "))
            while opcion1 < 1 and opcion1 > 2:
                print("ERROR")
                opcion1 = int(input("Elija: 1-Ingresar propiedad 2-Vender/Alquilar propiedad: "))
            if opcion1 == 1:
                tipo = int(input("Que tipo de propiedad desea ingresar? 1-Venta 2-Alquiler"))
                while tipo < 1 and tipo > 2:
                    print("ERROR")
                    tipo = int(input("Que tipo de propiedad desea ingresar? 1-Venta 2-Alquiler"))
                existe = True
                while existe:
                    existe = False
                    for i in agenciaInmobiliaria.propiedades:
                        if i.get_id_propiedad() == id_propiedad:
                            existe = True
                    id_propiedad = int(input("Ingrese la id: "))
                direccion = str(input("Ingrese la direccion: "))
                metros_cuadrados = int(input("Ingrese los m2: "))
                while metros_cuadrados < 1:
                    print("ERROR")
                    metros_cuadrados = int(input("Ingrese los m2: "))
                ambientes = int(input("Ingrese ambientes: "))
                while ambientes < 1:
                    print("ERROR")
                    ambientes = int(input("Ingrese ambientes: "))
                zona = str(input("Ingrese la zona: "))
                precio_base = int(input("Ingrese el precio base: "))
                while precio_base < 0:
                    print("ERROR")
                    precio_base = int(input("Ingrese el precio base: "))
                if tipo == 1:
                    comision = int(input("Ingrese la comision: "))
                    if comision < 0:
                        print("ERROR")
                        comision = int(input("Ingrese la comision: "))
                    propiedad = PropiedadVenta(id_propiedad,direccion,metros_cuadrados,ambientes,zona,precio_base,comision)
                elif tipo == 2:
                    expensas = int(input("Ingrese las expensas: "))
                    impuestos = int(input("Ingrese los impuestos: "))
                    mantenimiento = int(input("Ingrese los costos de mantenimiento: "))
                    while expensas < 0 and impuestos < 0 and mantenimiento < 0:
                        print("ERROR")
                        expensas = int(input("Ingrese las expensas: "))
                        impuestos = int(input("Ingrese los impuestos: "))
                        mantenimiento = int(input("Ingrese los costos de mantenimiento: "))
                    gastos_mensuales = (expensas,impuestos,mantenimiento)
                    propiedad = PropiedadAlquiler(id_propiedad,direccion,metros_cuadrados,ambientes,zona,precio_base,gastos_mensuales)
                agenciaInmobiliaria.agregar_propiedad(propiedad)
            elif opcion1 == 2:
                if agenciaInmobiliaria.clientes and agenciaInmobiliaria.propiedades:
                    x = 0
                    for i in agenciaInmobiliaria.clientes:
                        x+=1
                        print(f"{x})")
                        i.mostrar_info()
                    clienteOpcion = int(input("A que cliente le desea vender/alquilar una propiedad: "))
                    while clienteOpcion < 1 and clienteOpcion > len(agenciaInmobiliaria.clientes):
                        print("ERROR")
                        clienteOpcion = int(input("A que cliente le desea vender/alquilar una propiedad: "))
                    cliente = agenciaInmobiliaria.clientes[clienteOpcion-1]
                    opcion12 = int(input("Que desea realizar: 1-Vender propiedad 2-Alquilar propiedad: "))
                    while opcion12 < 1 and opcion12 > 2:
                        print("ERROR")
                        opcion12 = int(input("Que desea realizar: 1-Vender propiedad 2-Alquilar propiedad: "))
                    if opcion12 == 1:
                        for i in agenciaInmobiliaria.listar_disponibles("propiedad_venta"):
                            x+=1
                            print(f"{x})")
                            i.mostrar_info()
                        propiedadVender = int(input("Que propiedad desea vender? "))
                        while propiedadVender < 1 and propiedadVender > len(agenciaInmobiliaria.listar_disponibles("propiedad_venta")):
                            print("ERROR")
                            propiedadVender = int(input("Que propiedad desea vender? "))
                        propiedadVendida = agenciaInmobiliaria.listar_disponibles("propiedad_venta")[propiedadVender - 1]
                        propiedadVendida.estado = "vendida"
                    elif opcion12 == 2:
                        for i in agenciaInmobiliaria.listar_disponibles("propiedad_alquiler"):
                            x+=1
                            print(f"{x})")
                            i.mostrar_info()
                        propiedadAlquilar = int(input("Que propiedad desea alquilar? "))
                        while propiedadAlquilar < 1 and propiedadAlquilar > len(agenciaInmobiliaria.listar_disponibles("propiedad_alquiler")):
                            print("ERROR")
                            propiedadAlquilar = int(input("Que propiedad desea vender? "))
                        propiedadAlquilada = agenciaInmobiliaria.listar_disponibles("propiedad_alquiler")[propiedadAlquilar - 1]
                        propiedadAlquilada.estado = "alquilada"
                else:
                    print("No hay propiedades o clientes suficientes")
        elif opcion == 2:
            nombre = str(input("Ingrese el nombre: "))
            dni = int(input("Ingrese el dni: "))
            while dni < 0:
                print("ERROR")
                dni = int(input("Ingrese el dni: "))
            email = str(input("Ingrese el email: "))
            zona = str(input("Ingrese la zona que quiere: "))
            ambientes = int(input("Ingrese cantidad de ambientes que quiere: "))
            while ambientes < 1:
                print("ERROR")
                ambientes = int(input("Ingrese cantidad de ambientes que quiere: "))
            opcionTipo = int(input("Ingrese el tipo que quiere: 1-Venta 2-Alquiler: "))
            while opcionTipo < 1 and opcionTipo > 2:
                print("ERROR")
                opcionTipo = int(input("Ingrese el tipo que quiere: 1-Venta 2-Alquiler: "))
            if opcionTipo == 1:
                tipo = "propiedad_venta"
            elif opcionTipo == 2:
                tipo = "propiedad_alquiler"
            preferencias ={
                "zona":zona,
                "ambientes":ambientes,
                "tipo":tipo
            }
            cliente = Cliente(nombre,dni,email,preferencias)
            agenciaInmobiliaria.agregar_cliente(cliente)
        elif opcion == 3:
            opcion3 = int(input("Que desea realizar? 1-Ver propiedad 2-Ver disponibles por tipo 3-Filtrar propiedad por zona 4-Ver propiedad mas cara 5-Ver promedio de precios 6-Ver cliente interesado en propiedad: "))
            while opcion3 < 1 or opcion3 > 6:
                print("ERROR")
                opcion3 = int(input("Que desea realizar? 1-Ver propiedad 2-Ver disponibles por tipo 3-Filtrar propiedad por zona 4-Ver propiedad mas cara 5-Ver promedio de precios 6-Ver cliente interesado en propiedad: "))
            
            if opcion3 == 1:
                id_buscar = int(input("Ingrese el ID de la propiedad a buscar: "))
                propiedad = agenciaInmobiliaria.buscar_propiedad_id(id_buscar)
                if propiedad:
                    propiedad.mostrar_info()
                else:
                    print("Propiedad no encontrada")
            
            elif opcion3 == 2:
                tipo = int(input("Que tipo de propiedad desea ver? 1-Venta 2-Alquiler: "))
                while tipo < 1 or tipo > 2:
                    print("ERROR")
                    tipo = int(input("Que tipo de propiedad desea ver? 1-Venta 2-Alquiler: "))
                if tipo == 1:
                    tipo_str = "propiedad_venta"
                else:
                    tipo_str = "propiedad_alquiler"
                disponibles = agenciaInmobiliaria.listar_disponibles(tipo_str)
                for i, propiedad in enumerate(disponibles, 1):
                    print(f"\nPropiedad {i}:")
                    propiedad.mostrar_info()
            
            elif opcion3 == 3:
                zona = input("Ingrese la zona a filtrar: ")
                propiedades_zona = agenciaInmobiliaria.filtrar_por_zona(zona)
                for i, propiedad in enumerate(propiedades_zona, 1):
                    print(f"\nPropiedad {i}:")
                    propiedad.mostrar_info()
            
            elif opcion3 == 4:
                propiedad_cara = agenciaInmobiliaria.propiedad_mas_cara()
                print("Propiedad más cara:")
                propiedad_cara.mostrar_info()
            
            elif opcion3 == 5:
                promedio = agenciaInmobiliaria.promedio_precios()
                print(f"El promedio de precios es: ${promedio:.2f}")
            
            elif opcion3 == 6:
                id_propiedad = int(input("Ingrese el ID de la propiedad: "))
                propiedad = agenciaInmobiliaria.buscar_propiedad_id(id_propiedad)
                if propiedad:
                    clientes_interesados = agenciaInmobiliaria.clientes_interesados_en(propiedad)
                    if clientes_interesados:
                        print("Clientes interesados:")
                        x = 0
                        for i in clientes_interesados:
                            x+=1
                            print(f"{x})")
                            i.mostrar_info()
                    else:
                        print("No hay clientes interesados en esta propiedad")
                else:
                    print("Propiedad no encontrada")

if __name__ == "__main__":
    main()

#<>