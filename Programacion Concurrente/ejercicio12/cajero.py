class Cajero:
    id_cajero = 0
    def __init__(self,id):
        
        self.id = id
        self.saldo = 0
        self.clientes = []
        self.registro = ""

    def log(self, archivo, mensaje):
        with open(archivo, "a") as arch:
            arch.write(mensaje)

    def depositar(self, valor, id):
        if valor < 0:
            raise ValueError("No se pueden depositar valores negativos")
        self.saldo += valor
        self.log(f"cajero{self.id}.txt",f"El proceso {id} depositó una cantidad de:{valor}\n")

    def extraer(self,valor,id):
        if self.saldo < valor:
            raise ValueError("No se pueden retirar valores mayores al saldo")
        if valor < 0:
            raise ValueError("No se pueden retirar valores negativos")
        self.saldo -= valor
        self.log(f"cajero{self.id}.txt",f"El proceso {id} retiró una cantidad de:{valor}\n")
    
    def agregar_cliente(self,cliente):
        self.clientes.append(cliente)
    
    def guardar_estado_final(self):
        self.log(f"cajero{self.id}.txt", f"El estado final del saldo es de {self.saldo}")