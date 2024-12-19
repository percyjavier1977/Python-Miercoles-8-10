'''
Crear un programa donde debemos calcular una venta o factura.
'''
cliente = input("Ingrese el nombre del cliente: ").upper()
producto = input("Ingrese el nombre del producto: ").capitalize()
cantidad = int(input("Ingrese la cantidad de compra: "))
precio = float(input("Ingrese el precio del producto: "))

#Formulas

importe = cantidad * precio
#El descuento será el 3% del importe para todos los clientes
descuento = importe  *  3/100

total = importe - descuento

#Mostrar los resultados calculados

print("===========DETALLE DE LA VENTA==============")
print(f"CLIENTE--------------------------: {cliente}")
print(f"PRODUCTO-------------------------: {producto}")
print(f"CANTIDAD COMPRADA----------------: {cantidad}")
print(f"PRECIO DEL PRODUCTO--------------: S/{precio:.2f}")
print(f"IMPORTE--------------------------: S/{importe:.2f}")
print(f"EL IMPORTE DEL DESCUENTO AL 3% ES: S/{descuento:.2f}")
print(f"EL IMPORTE TOTAL ES--------------: S/{total:.2f}")
