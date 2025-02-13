try:
    numero = float(input("Ingrese un numero para dividir:"))
    divisor = float(input("Ingrese el divisor: "))
    resultado = numero / divisor
    print(resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
else:
    #Solo se ejecuta si no ocurre ningun error
    print("La división se ejecuto correctamente")
finally:
    print("Fin del sistema")