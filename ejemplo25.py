#Crear un programa que simule tirar un dato. El bucle cuntinuará hasta que salga 6.

import random
import time
dado = 0
intentos = 0
while dado !=6:
    dado = random.randint(1,6)
    print(f"El dado cayó en el número: {dado}")
    intentos +=1
    time.sleep(1)


print(f"El dado cayo en {dado} y ganaste")
print(f"Para ganar realizaste {intentos} intentos")