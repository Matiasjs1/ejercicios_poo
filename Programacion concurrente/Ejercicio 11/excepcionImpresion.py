class ExcepcionImpresion(Exception):
        def __init__(self, mensaje="La impresora falló al intentar imprimir el archivo"):
            super().__init__(mensaje)
            