#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
#la <n> entre <m> da un cociente <c> y
#un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
#y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("introduce el numero carajo: "))
m = int(input("Introduce el otro numero carajo: "))


#Calcular el cociente y el resto de la division entera 

c = n // m #Cociente de la division entera 
r = n % m #Resto de la division entera 

print(f'{n} entre {m} da un cociente de {c} y residuo de {r}')



