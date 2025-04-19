from calculadora import Calculadora

def main():
    print("Calculadora")
    try:
        precio = float(input("Ingrese su precio: "))
        descuento = float(input("Ingrese el descuento: "))
        
        calc = Calculadora(precio, descuento)
        precio_final = calc.calcular_precio_final()
        print(f"Precio final: ${precio_final: .2f}")
        
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except TypeError as te:
        print(f"Error de tipo; {te}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Programa finalizado")
        
if __name__ == "__main__":
        main()