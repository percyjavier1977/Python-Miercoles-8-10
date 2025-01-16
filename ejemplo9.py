#Crear un programa donde el sistema debe enviar un mensaje si esta apto para votar o no

nacionalidad = input("Ingrese su nacionalidad: ").lower()
edad = int(input("Ingrese su edad: "))

if nacionalidad == "peruano" and edad >17:
    print("Usted esta apto para votar")
else:
    print("usted no esta apto para votar")
