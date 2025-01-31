import random
puntos = 0
intentos_max = int(input("Configure el número de intenetos: "))
for intento in range(1,intentos_max+1):
    numero = random.randint(1,50)
    print(f"Intento N° {intento}")
    respuesta = input(f"¿El número {numero} es par o impar?..(Responde par o impar) ").lower()
    if (numero % 2 == 0 and respuesta == "par") or (numero % 2 != 0 and respuesta == "impar"):
        print("Correcto")
        puntos +=1

    else:
        print("Incorrecto")
        puntos -=1

else:
    print("Se acabaron los intentos")
    if puntos >=0:
        print(f"Tienes un total de {puntos} puntos")
    else:
        print("Debes puntos :)")