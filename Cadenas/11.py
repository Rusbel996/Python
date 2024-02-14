#Escribir un programa que pregunte el nombre el un producto, su precio y un 
#número de unidades y muestre por pantalla una cadena con el nombre del producto 
#seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de
#unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

Nombre = input("Cual es el nombre del producto: ")

Precio = float(input("Cual es le precio: "))

Unidades = input("Cual es la cantidad: ")


Cadena = [Nombre,Precio,Unidades]

print(Cadena)


# Solicitar al usuario que ingrese el nombre del producto, su precio y el número de unidades
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
unidades = int(input("Ingrese el número de unidades del producto: "))

# Calcular el costo total
costo_total = precio_unitario * unidades

# Formatear la cadena con el nombre del producto, su precio unitario y el número de unidades
cadena = "{}: {:>9.2f} {:>3} {:>12.2f}".format(nombre_producto, precio_unitario, unidades, costo_total)

# Mostrar la cadena por pantalla
print(cadena)
