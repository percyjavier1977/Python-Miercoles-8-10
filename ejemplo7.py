'''
Crear un programa para una casa de cambio. Al ejecutar el programa mostrar las opciones siguintes

1.Dolares
2.Soles
3.Euros
4.salir
'''
#Tasa de cambio
tasa_dolares = 3.75
tasa_euro = 4.15

#menu Principal
print("===Bienvenido a la Casa de Cambio===")
print("Por favor, elija el tipo de moneda de desea ingresar:")
print("1.Dólares")
print("2.Soles")
print("3.Euros")
print("4.Salir")

opcion = int(input("Ingrese el número de la opción:"))
if opcion == 1:
    cantidad = float(input("Ingrese la cantidad en dólare: "))
    dolares_soles = cantidad * tasa_dolares
    dolares_euros = dolares_soles / 4.15
    print(f"Los dolares a soles es: {dolares_soles:.2f} PEN")
    print(f"Los dólares a euros son: {dolares_euros:.2f} EUR") 
elif opcion == 2:
    cantidad = float(input("Ingres la cantidad en soles: "))
    soles_dolares = cantidad / tasa_dolares
    soles_euros = cantidad / tasa_euro
    print(f"Los soles a dolares son: {soles_dolares:.2f} USD")
    print(F"Los soles a euros son: {soles_euros:.2f} EUR")
elif opcion == 3:
    cantidad  = float(input("Ingrese la cantidad en euros: "))
    euros_soles = cantidad * tasa_euro
    euros_dolares = euros_soles / tasa_dolares
    print(f"Los euros a soles es: {euros_soles:.2f} PEN")
    print(f"Los euros a dolares son: {euros_dolares:.2f} USD")
elif opcion == 4:
    print("Saliendo del sistema........")
else:
    print("Opcion no existe...Intente nuevamente")

