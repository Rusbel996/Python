#Escribir un programa que pregunte por
#consola el precio de un producto en euros con dos decimales y muestre por
#pantalla el número de euros y el número de céntimos del precio introducido.

Precio_Producto = input("Cual es precio con dos decimales: ")

Entero , Decimal = Precio_Producto.split(',')

print(f'El precion entero del producto es {Entero} y la parte decimal es {Decimal}')

precio_str = input("Ingrese el precio del producto en euros (con dos decimales): ")

# Convertir el precio ingresado a tipo float
precio = float(precio_str)

# Calcular la parte entera (euros) y la parte decimal (céntimos) del precio
euros = int(precio)
centimos = int((precio - euros) * 100)

# Mostrar el número de euros y el número de céntimos del precio por pantalla
print("Número de euros:", euros)
print("Número de céntimos:", centimos)