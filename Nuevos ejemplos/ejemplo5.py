try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Error: debes ingresar un número: ")
    
else:
    print(f"El número ingresado es {numero}")