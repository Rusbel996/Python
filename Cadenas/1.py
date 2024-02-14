#Escribir un programa que pregunte el nombre del usuario en la consola 
#y un número entero e imprima por pantalla en líneas distintas
#el nombre del usuario tantas veces como el número introducido.

Nombre =  input("Cual estu nombre jorgito: ")

Numero = int(input("Cual es el numero carajo: "))


print(f'')

# Solicitar al usuario su nombre
nombre_usuario = input("Ingrese su nombre: ")

# Solicitar al usuario un número entero
numero_entero = int(input("Ingrese un número entero: "))

# Imprimir el nombre del usuario tantas veces como el número introducido
for _ in range(numero_entero):
    print(nombre_usuario)
    
    
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))    

