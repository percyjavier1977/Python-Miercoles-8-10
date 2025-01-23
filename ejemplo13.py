puntuacion = float(input("Ingrese su puntuación 0 - 100: "))
if puntuacion >=0 and puntuacion <=100:
    #Programar el sistemas
    if puntuacion <50:
        rendimiento = "Insufuciente"
    elif 50<= puntuacion <60:
        rendimiento = "Suficiente"
    elif 60<= puntuacion <80:
        rendimiento = "Bueno"
    elif 80<= puntuacion <90:
        rendimiento = "Muy bueno"
    else:
        rendimiento = "Excelente"

    print(f"Tu puntuación es: {puntuacion:.1f}")
    print(f"Categoria de rendimiento: {rendimiento}")

else:

    print("¡ERROR!..Ingrese un número entre 0-100")

