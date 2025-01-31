'''
Un programa donde el usuario ingresa la contraseña hastas 3 veces.
'''

for i in range(1,4):
    c = 12345
    print(f"Intento N° {i}")
    contra = int(input("Ingerse la contraseña: "))
    
    if contra == c:
        print("Contraseña correcta..Ingresando al sistemas")
        break #Cierra el bucle
    else:
        
        print("Contraseña incorrecta")
else:
    print("Realizó sus 3 intentos.....TARJETA BLOQUEDA")