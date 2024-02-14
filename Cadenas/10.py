#Escribir un programa que pregunte por consola por 
#los productos de una cesta de la compra, separados por comas
#, y muestre por pantalla cada uno de los productos en una línea distinta.

Cesta = input("Cuantos productos hay en la cesta: ")


Productos = Cesta.split(',')


print(f'los productos de la cesta son {Productos} ')



# Solicitar al usuario que ingrese los productos separados por comas
productos = input("Ingrese los productos de la cesta de la compra separados por comas: ")

# Dividir la cadena de productos en una lista utilizando la coma como separador
productos_lista = productos.split(",")

# Mostrar cada producto en una línea distinta
for producto in productos_lista:
    print(producto.strip())  # Utilizamos strip() para eliminar espacios en blanco alrededor del producto, si los hay
    