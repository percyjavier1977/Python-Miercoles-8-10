#Crear un programa donde el usuario ingresa un número de cuantas notas va a ingresar
#al sistema. Debe mostrar el puntaje, el promedio, nota maxima, nota minima
nota_maxima = float('-inf')
nota_minima = float('inf')
nnotas = int(input("¿Cuantas notas va a ingresar?: "))

if nnotas >=2:
   
    suma_notas = 0
    for i in range(1,nnotas+1):
        nota = int(input(f"Ingrese la nota {i}: "))
        suma_notas += nota


        if nota > nota_maxima:
            nota_maxima = nota
        
        if nota < nota_minima:
            nota_minima = nota

    promedio = suma_notas / nnotas
    print(f"El puntaje es: {suma_notas}")
    print(f"El promedio es: {promedio:.2f}")
    print(f"La nota máxima: {nota_maxima}")
    print(f"Nota mínima: {nota_minima}")
else:
    print("¡ERROR...Se debe ingresar mínimo 2 notas")

