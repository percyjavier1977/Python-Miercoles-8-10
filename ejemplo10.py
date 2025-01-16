#Crear un programa donde valide una nota ingresada. Si la nota no esta entre 0 y 20 debe mostrar
#un mnesaje de error.

nota = int(input("Ingrese la nota entre 0 y 20: "))
if nota >=0 and nota <=20:
    print("Ingreso correctamente la nota")
else:
    print("¡ERROR!..Nota no válida")



nota = int(input("Ingrese la nota entre 0 y 20: "))
if 0 <= nota <= 20: # Parametros
     print("Ingreso correctamente la nota")
else:
    print("¡ERROR!..Nota no válida")