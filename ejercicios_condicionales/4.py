#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar

Numero = int(input("Ingrese un numero entero: "))


#10 % 3 devuelve 1 porque 10 dividido por 3 es 3 con un residuo de 1.
#8 % 2 devuelve 0 porque 8 dividido por 2 es 4 sin residuo.

if Numero % 2 == 0: 
    print(f'el numero {Numero} es par')
    
else :
    print(f'el numero {Numero} es impar')    