num = 0
num = float(input("ingrese un numero, si es positivo seguimos...., cero o negativo para terminar: "))
while num>0:
    if (num>0):
        print("numero no es negativo ....")
        num = float(input("ingrese un numero mayor o igual a 0: "))

print("el numero es: ",num)