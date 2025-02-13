contador = 0
CONTRA = "12345peru"
while True:
    contraseña = input("Ingrese la contraseña: ").lower()
    contador+=1
    if contraseña == CONTRA:
        print("Contraseña correcta.Ingresando al Sistema")
        break
    else:
        print("Contraseña incorrecta")
    
    
    print(f"Número de intentos {contador}")