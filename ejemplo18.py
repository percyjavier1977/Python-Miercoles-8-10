#Crear un programa donde el usuario ingresa un número de cuantas notas va a ingresar
#al sistema. Debe mostrar el puntaje, el promedio, nota maxima, nota minima

nnotas = int(input("¿Cuantas notas va a ingresar?: "))
if nnotas >=2:
    suma_notas = 0
    for i in range(1,nnotas+1):
        nota = int(input(f"Ingrese la nota {i}: "))
        suma_notas += nota


    promedio = suma_notas / nnotas
    print(f"El puntaje es: {suma_notas}")
    print(f"El promedio es: {promedio:.2f}")
else:
    print("¡ERROR...Se debe ingresar mínimo 2 notas")