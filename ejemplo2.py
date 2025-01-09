'''
Crear un programa donde se genere una venta. Debemos aplicar dos descuentos
Descunto 1 = si el importe de la venta supera los 250 soles el descuento será el 2.5 % 
del importe.
Descuento 2 = si compró mas de de 5 unidades se le descontará el 2% del importe.
'''
cliente = input("Ingrese el nombre del cliente: ").upper()
producto = input("Ingrese el producto: ").upper()
cantidad = int(input("Ingrese la cantidad: "))
precio = float(input("Ingres el precio del producto: "))
descuento1 = 0
descuento2 = 0
#Calcular el importe
importe = cantidad * precio

if importe > 250:
    #si es verdad
    descuento1 = importe * (2.5/100)

if cantidad > 5:
    descuento2 = importe * (2/100)
    

importe_total = importe - (descuento1+descuento2)
#Mostrar los resultados
print("\n-------DETALLE DEL LA VENTA---------")
print("Cliente:----------------------",cliente)
print("Producto:--------------------",producto)
print("Cantidad:--------------------",cantidad)
print(f"Precio:--------------------- S/{precio:.2f}")
print(f"Importe:-------------------- S/{importe:.2f}")
print(f"Descuento 1:---------------- S/{descuento1:.2f}")
print(f"Descuento 2:---------------- S/{descuento2:.2f}")
print(f"Total a pagar:-------------- S/{importe_total:.2f}")









    
