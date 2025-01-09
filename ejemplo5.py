'''
Crear un programa para una institución educativa:
El sistema debe calcular el promedio de tres notas y debe mostrar si al alumnos esta aprobado
o desaprobado. Tambien debe mostrar la nota mayor y menor.
esta aprobado si su promedio es mayor a 12.

'''
alumno = input("Ingrse el nombre del alumnos: ").capitalize()
curso = input("Ingrese el curso: ").capitalize()

n1 = float(input("Ingrese la Nota 1: "))
n2 = float(input("Ingrese la Nota 2: "))
n3 = float(input("Ingrese la Nota 3: "))

promedio = (n1+n2+n3)/3
promedio = round(promedio,0)

if promedio > 12:
    obs = "Aprobado"
else:
    obs = "Desaprobado"


nota_maxima = max(n1,n2,n3) #Función que muestra el valor mayor de números.
nota_minima = min(n1,n2,n3)

print("-------BOLETA DE NOTAS------")
print(f"NOTA 1: {n1}")
print(f"NOTA 2: {n2}")
print(f"NOTA 3: {n3}")
print(f"PROMEDIO: {promedio}")
print(f'Alumn@ {alumno} usted esta "{obs}"')
print()
print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")

