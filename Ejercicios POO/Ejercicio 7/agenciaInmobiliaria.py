from cliente import Cliente
from propiedadVenta import PropiedadVenta
from propiedadAlquiler import PropiedadAlquiler
import os

class AgenciaInmobiliaria:
    def __init__(self):
        self.propiedades = []
        self.clientes = []

    def agregar_propiedad(self):
        direccion = str(input("Ingrese la dirección de la propiedad: "))
        metrosC = int(input("Ingrese los metros cuadrados de la propiedad: "))
        if metrosC < 1:
            print("Error")
            metrosC = int(input("Ingrese los metros cuadrados de la propiedad: "))
        ambientes = int(input("Ingrese la cantidad de ambientes de la proiedad: "))
        if ambientes < 1:
            print("Error")
            ambientes = int(input("Ingrese la cantidad de ambientes de la proiedad: "))
        zona = str(input("Ingrese la zona de la propiedad: "))
        precio_base = float(input("Ingrese el precio base de la propiedad: "))
        if precio_base <= 0:
            print("Error")
            precio_base = float(input("Ingrese el precio base de la propiedad: "))
        tipo = int(input("¿La propiedad está para vender o alquilar? 1-Vender 2-Alquilar: "))
        if tipo != 1 and tipo != 2:
            print("Error")
            tipo = int(input("¿La propiedad está para vender o alquilar? 1-Vender 2-Alquilar: "))
        if tipo == 1:
            estadoElección = int(input("Ingrese el estado de la propiedad: 1-Disponible, 2-Reservada, 3-Vendida: "))
            if estadoElección < 1 or estadoElección > 3:
                print("Error")
                estadoElección = int(input("Ingrese el estado de la propiedad: 1-Disponible, 2-Reservada, 3-Vendida: "))
            if estadoElección == 1:
                estado = "Disponible"
            elif estadoElección == 2:
                estado = "Reservada"
            elif estadoElección == 3:
                estado = "Vendida"
            comision = float(input("Ingrese el porcentaje de comisión: "))
            if comision <=0:
                print("Error")
                comision = float(input("Ingrese el porcentaje de comisión: "))
            propiedad = PropiedadVenta(direccion, metrosC, ambientes, zona, precio_base, estado, comision)
        elif tipo == 2:
            estadoElección = int(input("Ingrese el estado de la propiedad: 1-Disponible, 2-Reservada, 3-Alquilada: "))
            if estadoElección < 1 or estadoElección > 3:
                print("Error")
                estadoElección = int(input("Ingrese el estado de la propiedad: 1-Disponible, 2-Reservada, 3-Vendida: "))
            if estadoElección == 1:
                estado = "Disponible"
            elif estadoElección == 2:
                estado = "Reservada"
            elif estadoElección == 3:
                estado = "Alquilada"
            expensas = float(input("Ingrese el precio de las expensas por mes: "))
            if expensas < 0:
                print("Error")
                expensas = float(input("Ingrese el precio de las expensas por mes: "))
            impuestos = float(input("Ingrese el precio de los impuestos por mes: "))
            if impuestos < 0:
                print("Error")
                impuestos = float(input("Ingrese el precio de los impuestos por mes: "))
            mantenimiento = float(input("Ingrese el precio del mantenimiento por mes: "))
            if mantenimiento < 0:
                print("Error")
                mantenimiento = float(input("Ingrese el precio del mantenimiento por mes: "))
            propiedad = PropiedadAlquiler(direccion, metrosC, ambientes, zona, precio_base, estado, expensas, impuestos, mantenimiento)
        self.propiedades.append(propiedad)
        print("Se agregó una propiedad")

    def agregar_cliente(self):
        nombre = str(input("Ingrese el nombre del cliente: "))
        dni = int(input("Ingrese el DNI del cliente: "))
        if dni <= 0:
            print("Error")
            dni = int(input("Ingrese el DNI del cliente: "))
        email = str(input("Ingrese el email del cliente: "))
        zona = str(input("Ingrese la zona de preferencia del cliente: "))
        ambientes = int(input("Ingrese la cantidad de ambientes de preferencia del cliente: "))
        if ambientes <= 0:
            print("Error")
            ambientes = int(input("Ingrese la cantidad de ambientes de preferencia del cliente: "))
        tipoEleccion = int(input("¿Qué prefiere el cliente? 1-Alquiler, 2-Venta: "))
        if tipoEleccion < 1 or tipoEleccion > 2:
            print("Error")
            tipoEleccion = int(input("¿Qué prefiere el cliente? 1-Alquiler, 2-Venta: "))
        if tipoEleccion == 1:
            tipo = "Alquiler"
        elif tipoEleccion == 2:
            tipo = "Venta"
        nuevoCliente = Cliente(nombre, dni, email, zona, ambientes, tipo)
        self.clientes.append(nuevoCliente)

    def buscar_propiedad_por_id(self):
        id = int(input("Ingrese la id de la propiedad que quiere buscar: "))
        propiedad = None
        for i in self.propiedades:
            if i.id_propiedad == id:
                propiedad = i
        if propiedad == None:
            print("No se encontró dicha propiedad")
        else:
            print("Se encontró la siguiente propiedad: ")
            propiedad.mostrar_info()

    def listar_disponibles(self): #puede filtrar por venta o alquiler
        listaA = []
        eleccion = int(input("¿Desea listar propiedades en venta o en alquiler? 1-Venta 2-Alquiler: "))
        if eleccion != 1 and eleccion != 2:
            print("Error")
            eleccion = int(input("¿Desea listar propiedades en venta o en alquiler? 1-Venta 2-Alquiler: "))
        if eleccion == 1:
            for i in self.propiedades:
                if i.estado == "Disponible" and type(i) == PropiedadVenta:
                    listaA.append(i)
        elif eleccion == 2:
            for i in self.propiedades:
                if i.estado == "Disponible" and type(i) == PropiedadAlquiler:
                    listaA.append(i)
        if len(listaA) == 0:
            print("No se encontró ninguna propiedad")
        else:
            print("Las propiedades encontradas fueron: ")
            for i in listaA:
                i.mostrar_info()
        
    def filtrar_por_zona(self):
        listaA = []
        zona = str(input("Ingrese la zona por la que quiere buscar: "))
        for i in self.propiedades:
            if i.zona == zona:
                listaA.append(i)
        if len(listaA) == 0:
            print("No se encontró ninguna propiedad")
        else:
            print("Las propiedades encontradas fueron: ")
            for i in listaA:
                i.mostrar_info()

    def propiedad_mas_cara(self):
        if len(self.propiedades) > 0:
            propiedadMasCara = self.propiedades[0]
            for i in self.propiedades:
                if i.calcularPrecioFinal() > propiedadMasCara.calcularPrecioFinal():
                    propiedadMasCara = i
            print("La propiedad más cara es: ")
            propiedadMasCara.mostrar_info()
        else:
            print("Aún no hay propiedades registradas")
        
    def promedio_precios(self, tipo):
        total = 0
        cantidad = 0
        if tipo == "Alquiler":
            filtro = PropiedadAlquiler
        elif tipo == "Venta":
            filtro = PropiedadVenta
        for i in self.propiedades:
            if type(i) == filtro:
                cantidad += 1
                total += i.calcularPrecioFinal()
        if cantidad == 0:
            print(f"No se encontraron propiedades en {tipo}")
        else:
            print(f"El promedio de precios es de: ${total/cantidad}")


    def clientes_interesados_en(self, propiedad): #analiza cuántos clientes tienen coincidencia con esa propiedad    
        listaInteresados = []
        for i in self.clientes:
            listaInteresesCliente = i.coincidencias(self.propiedades)
            if propiedad in listaInteresesCliente:
                listaInteresados.append(i)
        if listaInteresados == 0:
            print("No hay interesados en la propiedad")
        else:
            print(f"Hay {len(listaInteresados)} clientes interesados en tu propiedad")

    def reporte_general(self): #muestra resumen de propiedades disponibles, vendidas y alquiladas, total ganado por ventas y total proyectado por alquileres.
        cantDisponibles = 0
        cantVendidas = 0
        cantAlquiladas = 0
        totalVentas = 0
        totalAlquiler = 0
        for i in self.propiedades:
            if i.estado == "Disponible":
                cantDisponibles += 1
            elif i.estado == "Vendida":
                cantVendidas += 1
                totalVentas += i.calcularPrecioFinal()
            elif i.estado == "Alquilada":
                cantAlquiladas += 1
                totalAlquiler += i.calcularPrecioFinal()
        print(f"Propiedades disponibles: {cantDisponibles}\nPropiedades vendidas: {cantVendidas}\nPropiedades alquiladas: {cantAlquiladas}\nTotal ganado por ventas: {totalVentas}\nTotal ganado por alquileres (por mes): {totalAlquiler}")