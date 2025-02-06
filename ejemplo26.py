#En el juego del dado debemos limitar 5 intentos

import random
import time
pregunta = "s"
contador = 0
jugador = input("Ingrese su nombre: ").upper()
while pregunta == "s":
    dado = 0
    intentos = 0
    intentos_max = 5

    while dado !=6 and intentos < intentos_max:
        dado = random.randint(1,6)
        print(f"El dado cayó en: {dado}")
        intentos+=1
        time.sleep(1)

    if dado == 6:
        print(f"Sacaste el número {dado} en el intento {intentos}....¡GANASTE!")
    else:
        print(f"No salio el 6 despues de {intentos} intenetos..¡PERDISTE!")

    contador+=1
    time.sleep(1)
    pregunta = input("¿Quiere volver a jugar? (s/n): ").lower()

print(f"{jugador} has jugado {contador} veces ")
print(f"¡Gracias por Jugar! {jugador}")
