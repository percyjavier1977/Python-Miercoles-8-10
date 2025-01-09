'''
Crear una aplicación donde se ingre la edad de una persona y debe mostrar el siguiente
mensaje. Si es mayor de edad "Usted puede ingresar al avento", si es menor de edad
"Usted no puede ingresar al evento.
'''
edad = int(input("Ingresa la edad de la persona:\n"))
if edad >17:
    mensaje = "Usted puede ingresar al evento"
else:
    mensaje = "¡ALARMA!..Usted no puede ingresar al evento"
    
print("---AVISO DEL SISTEMA---")
print(mensaje.upper())
