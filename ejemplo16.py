#Mostrar la tabla del 1 al 12 de un número ingresado

numero = int(input("Ingrese un número:"))
if numero > 0:
    print(f"======TABLA DE MULTIPLICAR DEL {numero} ==========")
    for i in range(1,13):
        m = i * numero
        print(f"{i} X {numero} = {m}")
else:
    print("¡ERROR...Ingrese numeros mayores a cero")