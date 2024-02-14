#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada 
#paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y
#muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


Payasos = int(input("Cual es la cantidad de payasos: "))

Muñecas = int(input("Cual es la cantidad de muñecas: "))

Peso_Payasos = 112

Peso_Muñecas = 75 

Peso_Paquete = Payasos*Peso_Payasos + Muñecas*Peso_Muñecas

print(f'el peso total del paquete es {Peso_Paquete} gramos')