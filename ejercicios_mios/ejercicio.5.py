#Escribir un programa que lea un entero positivo, 
#, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
#. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:


n = float(input("Ingrese un numero carajo: "))


suma = ((n * (n + 1)) / 2)

print(f'la suma de los numeros es {suma}')

suma = 0
for i in range(1, 11):
    suma += i

print("La suma de los números del 1 al 10 es:", suma)


numeros = list(range(1, 11))
suma = sum(numeros)

print("La suma de los números del 1 al 10 es:", suma)






