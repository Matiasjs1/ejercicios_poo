a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))
c = int(input("Ingrese un número: "))

numMayor = a

if b > numMayor:
    numMayor = b

if c > numMayor:
    numMayor = b

print(f"El número mayor es: {a}")