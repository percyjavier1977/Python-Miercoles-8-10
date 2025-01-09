'''
Crear una aplicación que muestre 4 opciones
la pirmera opcion para calcular el area de un circulo
la segunda opcion para calcular el area de un cuadrado
la tercera calcular el area de un rectangulo.
'''
import math
print("---SISTEMA DE CALCULOS MATEMÁTICOS------")
print("Seleccione una opción:")
print("1. Calcular el área de un círculo")
print("2. Calcular el área de un cuadrado")
print("3. Calcualar el áre del un rectangulo")

opcion = int(input("Ingrese el número de la opción (1-3): "))
if opcion == 1:
    radio = float(input("Ingrese el radio del circulo: "))
    area = math.pi * radio ** 2
    print(f"El área del circulo es {area:.2F}")
elif opcion == 2:
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado**2
    print(f"El área del cuadrado es: {area:.2F}")
elif opcion == 3:
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la aultura del rectángulo: "))
    area = base * altura
    print(f"El área del rectangulo es {area:.2f}")
else:
    print("¡ERROR!......Opcion no existe")
    
