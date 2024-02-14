#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el 
#día tiene un descuento del 60%. Escribir un programa que comience leyendo 
#el número de barras vendidas que no son del día. 
#Después el programa debe mostrar el precio habitual de una barra de pan,
#el descuento que se le hace por no ser fresca y el coste final total.


pan_del_dia = int(input("Ingrese el numero de panes del dia: "))

pan_pasado = int(input("Ingrese la cantidad de panes pasados"))


Precio = 3.49

Descuento = 0.6

Precio_Descuento = Precio * Descuento

Costo_total = pan_pasado * Precio * (1 - Descuento)

print(f'el precio normal del pan es {Precio} y como la cantidad de panes es {pan_pasado} y el costo total {Costo_total} ')


barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")