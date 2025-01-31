import random
numero_adivinar = random.randint(1,10)
intentos_max = 3

for i in range(1,intentos_max+1):
    numero_ingresado = int(input(f"Intento {i}.....Ingrese un número entre 1 - 5: "))
    if numero_ingresado == numero_adivinar:
        print("¡Felicitaciones! Adivinaste el número")
        break
    else:
        if i < 3:
            print("Sigue intentando...")

else:
    print("Lo siento has perdido el juego")
    print(f"El número de la suerte era: {numero_adivinar}")

