try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        raise ValueError("La edad no debe ser un número negativo")
except ValueError as e:
    print("¡ERROR",e)
else:
    print(f"Ingreso la edad {edad}")