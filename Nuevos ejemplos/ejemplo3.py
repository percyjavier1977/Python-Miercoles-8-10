
import time
import os
pin = "1234"
saldo = 6000
intentos = 3

while intentos > 0:
    pin_ingreso = input("Ingrese su PIN: ")
    if pin_ingreso == pin:
        print("PIN Correcto. Bienvenido al cajero")
        break
    else:
        intentos -=1
        if intentos >0:
            print(f"PIN incorrecto.te quedan {intentos} intentos")
    
if intentos == 0:
    print("Has agotado todos los intenetos. ¡TARJETA BLOQUEDA!")
    
else:
    #menu de opciones
   
    while True:
        os.system("cls")
        print("========MENU DEL CAJERO========")   
        print("1.Consultar saldo")
        print("2. Retirar dinero")
        print("3. Salir")
        opcion = input("Ingrese la opción (1-3): ")
        if opcion == "1":
            print(f"Su saldo disponible es: S/{saldo:.2f} ")
            time.sleep(4)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= saldo:
                saldo -=monto
                print(f"Has retirado {monto:.2f} soles. Tu nuevo saldo es {saldo:.2f}")
                time.sleep(4)
            else:
                print("Saldo insufuciente")
                time.sleep(4)
        elif opcion == "3":
            print("GRACIAS por usar el cajero automático")
            break
        else:
            print("Opción no válida. Intente nuevamente")
            
        
        