#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

A = input("Introduce el numero A: ")
B = input("Introduce el numero B: ")


Divison = A // B 

if A == 0:
    print("ERROR CARAJO")
    
else: 
    print(Divison)    