from campaniaRedesSociales import CampaniaRedesSociales
from campaniaSEO import CampaniaSEO
import os

class AgenciaMarketing:
    def __init__(self):
        self.campanias = []
    
    def agregarCampania(self, cliente, presupuesto, duracion, tipo):
        if tipo == "CampaniaRedesSociales":
            campania = CampaniaRedesSociales(cliente, presupuesto, duracion)
            for i in range(1, duracion +1):
                os.system("cls")
                print(f"Dia {i}")
                cantidad = int(input(f"Ingrese la cantidad de interacciones del dia: "))
                while cantidad < 0:
                    print("Valor incorrecto")
                    cantidad = int(input("Ingrese la cantidad: "))
                campania.registrar_interacciones_sociales(i, cantidad)
                
                clicks = int(input("Ingrese los clicks que se hicieron en el día: "))
                while clicks < 0:
                    print("Valor incorrecto")
                    clicks = int(input("Ingrese los clicks que se hicieron en el día: "))
                conversiones = int(input("Ingrese las conversiones del día: "))
                while conversiones < 0:
                    print("Valor incorrecto")
                    conversiones = int(input("Ingrese las conversiones del día: "))
                costo_dia = float(input("Ingrese el costo del dia: "))
                while costo_dia < 0:
                    print("Valor incorrecto")
                    costo_dia = int(input("Ingrese el costo del dia: "))
                campania.registrar_resultado(i, clicks, conversiones, costo_dia)


        elif tipo == "CampaniaSEO":
            campania = CampaniaSEO(cliente, presupuesto, duracion)
            salir = False
            while not salir:
                registrarPalabra = int(input("Desea registrar una palabra clave efectiva: 1-Si 2-No: "))
                while registrarPalabra != 1 and registrarPalabra != 2:
                    print("Valor incorrecto")
                    registrarPalabra = int(input("Desea registrar una palabra clave efectiva: 1-Si 2-No: "))
                if registrarPalabra == 1:
                    palabra = str(input("Ingrese la palabra clave: "))
                    campania.agregar_palabras_clave_efectivas(palabra)
                elif registrarPalabra == 2:
                    salir = True
            
            for i in range(1, duracion +1):
                os.system("cls")
                print(f"Dia {i}")
                clicks = int(input("Ingrese los clicks que se hicieron en el día: "))
                while clicks < 0:
                    print("Valor incorrecto")
                    clicks = int(input("Ingrese los clicks que se hicieron en el día: "))
                conversiones = int(input("Ingrese las conversiones del día: "))
                while conversiones < 0:
                    print("Valor incorrecto")
                    conversiones = int(input("Ingrese las conversiones del día: "))
                costo_dia = float(input("Ingrese el costo del dia: "))
                while costo_dia < 0:
                    print("Valor incorrecto")
                    costo_dia = int(input("Ingrese el costo del dia: "))
                campania.registrar_resultado(i, clicks, conversiones, costo_dia)
        
        
        
        else:
            print("Error, tipo de campaña inexistente")
        
        self.campanias.append(campania)

    def listarCampania(self, tipo):
        listaA = []
        for i in self.campanias:
            if type(i) == tipo:
                listaA.append(i)
        return listaA
    
    def calcularRanking(self):
        ranking = []
        campanias = self.campanias.copy()
        MayorVariable = campanias[0]
        
        while len(campanias) != 0:
            for i in campanias:
                if i.eficiencia() > MayorVariable.eficiencia():
                    MayorVariable = i
            ranking.append(i)
            campanias.remove(i)
        return ranking
    
    def calcularClienteMasROI(self):
        ROI_mayor = 0
        clienteMayor = None
        for i in self.campanias:
            ROIresultado = (i.calcular_conversion_total() * 10) / i.calcular_costo_total()
            if ROIresultado > ROI_mayor:
                ROI_mayor = ROIresultado
                clienteMayor = i.cliente
        print(f"El cliente con más ROI es: {clienteMayor}")
        if ROI_mayor >= 100:
            print("Tiene un ROI alto")
        else:
            print("Tiene un ROI bajo")
        return clienteMayor
            

        
    def campaniaMayorEficiencia(self):
        if len(self.campanias) == 0:
            print("Aún no hay campañas")
        else:
            campaniaMayorEficiencia = self.campanias[0]
            for i in self.campanias:
                if i.eficiencia() > campaniaMayorEficiencia.eficiencia():
                    campaniaMayorEficiencia = i
            campaniaMayorEficiencia.mostrar_info()
            return campaniaMayorEficiencia
    
    def mostrar_informe_general(self, cliente):
        print(f"Nombre del cliente: {i.cliente}")
        for i in self.campanias:
            if i.cliente == cliente:
                if type(i) == CampaniaSEO:
                    tipoCampania = "SEO"
                elif type(i) == CampaniaRedesSociales:
                    tipoCampania = "Redes Sociales"
                ROIresultado = (i.calcular_conversion_total() * 10) / i.calcular_costo_total()
                print(f"Tipo de campaña: {tipoCampania}\nEficiencia: {i.eficiencia()}\nROI: {ROIresultado}")