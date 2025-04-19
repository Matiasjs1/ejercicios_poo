class AgenciaInmobiliaria:
    def __init__(self):
        self.propiedades = []
        self.clientes = []
    
    def agregar_propiedad(self,propiedad):
        self.propiedades.append(propiedad)
    
    def agregar_cliente(self,cliente):
        self.clientes.append(cliente)
    
    def buscar_propiedad_id(self,id):
        propiedad = None
        for i in self.propiedades:
            if i.get_id_propiedad() == id:
                propiedad = i
        return propiedad

    def listar_disponibles(self,tipo):
        lista = []
        if tipo == None:
            for i in self.propiedades:
                if i.estado == "disponible":
                    lista.append(i)
        else:
            for i in self.propiedades:
                if i.estado == "disponible" and i.tipo == tipo:
                    lista.append(i)
        return lista

    def filtrar_por_zona(self,zona):
        lista = []
        for i in self.propiedades:
            if i.zona == zona:
                lista.append(i)
        return lista
    
    def propiedad_mas_cara(self):
        propiedadCara = self.propiedades[0]
        for i in self.propiedades:
            if i.calcular_precio_final() > propiedadCara.calcular_precio_final():
                propiedadCara = i
        return propiedadCara

    def promedio_precios(self):
        total = 0
        for i in self.propiedades:
            total += i.calcular_precio_final()
        return total/len(self.propiedades)

    def clientes_interesados_en(self,propiedad):
        clientes_interesados = []
        for cliente in self.clientes:
            coincidencias = cliente.coincidencias([propiedad])
            if coincidencias:
                clientes_interesados.append(cliente)
        return clientes_interesados

    #metodos agregados para el reporte general:
    def listar_vendidas(self):
        vendidas = []
        for i in self.propiedades:
            if i.estado == "vendida":
                vendidas.append(i)
        return vendidas

    def listar_alquiladas(self):
        alquiladas = []
        for i in self.propiedades:
            if i.estado == "alquilada":
                alquiladas.append(i)
        return alquiladas

    def total_precio_vendidas(self):
        total_vendidas = 0
        for i in self.propiedades:
            if i.estado == "vendida":
                total_vendidas += i.calcular_precio_final()
        return total_vendidas
    
    def total_precio_alquiladas(self):
        total_alquiladas = 0
        for i in self.propiedades:
            if i.estado == "alquilada":
                total_alquiladas += i.calcular_precio_final()
        return total_alquiladas

    def reporte_general(self):        
        print(f"Propiedades disponibles: {len(self.listar_disponibles(self,None))}\nPropiedades vendidas: {len(self.listar_vendidas())}\nPropiedades alquiladas: {len(self.listar_alquiladas())}\nTotal ganado por ventas: ${self.total_precio_vendidas()}\nTotal proyectado por alquileres: ${self.total_precio_alquiladas()}")
        


#<>