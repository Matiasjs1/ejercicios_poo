import threading as th

class Buffer:
    def __init__(self):
        self.cola = []
        self.esperas = 0
        self.limite = 5
        self.condicion = th.Condition()

    def registro(self,archivo,mensaje):
        with open(archivo,"a") as a:
            a.write(mensaje+"\n")
        
    def producir(self, dato):
        with self.condicion:
            if len(self.cola) >= self.limite:
                self.esperas += 1
                self.condicion.wait()
            self.cola.append(dato)
            if len(self.cola) == 1:
                self.condicion.notify_all()
            self.registro("valores_ingresados.txt", f"Se ingresó el dato: {dato}")           
    
    def consumir(self):
        with self.condicion:
            if len(self.cola) == 0:
                self.esperas += 1
                self.condicion.wait()
            dato = self.cola.pop(0)
            if len(self.cola) == 4:
                self.condicion.notify_all()
            if not isinstance(dato, int):
                raise TypeError("El dato no es numérico")
            self.registro("valores_procesados.txt", f"Se procesó el dato: {dato}")
            
            
