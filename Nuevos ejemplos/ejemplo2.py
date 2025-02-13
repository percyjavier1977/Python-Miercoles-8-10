import time
import os

TASA_DOLAR = 3.8
TASA_EUROS = 4.10


while True:
    #Limpiar la consola
    os.system('cls'if os.name=='nt' else 'clear')
    soles = float(input("Ingrese la cantidad en soles (o 0 para salir): "))
    if soles == 0:
        print("Programa finalizado")
        break
    
    #Mostrar el menú
    print("Seleccione una opción de tipo de cambio")
    print("1. Convertir a dólares")
    print("2. Covertir a euros")
    print("3. Converir a ambas monedas")
    print("4. Abrir la calculadora")
    print("5. Salir")
    
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        dolares = soles / TASA_DOLAR
        print(f"{soles} soles equivale a {dolares:.2f} Dólares.")
    elif opcion == 2:
        euros = soles / TASA_EUROS
        print(f"{soles} soles equivale a {euros:.2f} Euros.")
    elif opcion == 3:
        dolares = soles / TASA_DOLAR
        euros = soles / TASA_EUROS
        print(f"{soles} soles equivale a {dolares:.2f} Dólares.")
        print(f"{soles} soles equivale a {euros:.2f} Euros.")
    elif opcion == 4:
        os.system("calc")
    elif opcion == 5:
        print("Cerrando el sistema")
        break
    else:
        print("Opcion invalida")
        
    time.sleep(4)