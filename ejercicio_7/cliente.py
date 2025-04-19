class Cliente:
    def __init__(self,nombre,dni,email,preferencias):
        self.nombre = nombre
        self.__dni = dni
        self.email = email
        self.preferencias = preferencias

    def mostrar_preferencias(self):
        for i,x in self.preferencias.items():
            print(f"{i}: {x}")
    
    def coincidencias(self,propiedades):
        coincidencias = []             
        for i in propiedades:
            zona = False
            ambientes = False
            tipo = False
            if i.zona == self.preferencias["zona"]:
                zona = True
            if i.ambientes == self.preferencias["ambientes"]:
                ambientes = True
            if i.tipo == self.preferencias["tipo"]:
                tipo = True
            if zona and ambientes and tipo:
                coincidencias.append(i)
        return coincidencias
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nDNI: {self.__dni}\nEmail: {self.email}\nPreferencias:")
        self.mostrar_preferencias()
            
