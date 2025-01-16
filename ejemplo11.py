#Calcular el IMC y su obervación


peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = peso / (pow(altura,2)) #Función de potencia
imc = peso / (altura**2)

if imc < 18.5:
    obs = "Bajo de peso"
elif imc >=18.5 and imc < 25:
    obs = "Normal"
elif imc >=25 and imc < 30:
    obs = "Sobre peso"
else:
    obs = "Obesidad"

print(f"Tu IMC es: {imc:.2f}")
print(f"Observación: {obs}")