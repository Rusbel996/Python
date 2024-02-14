#Escribir un programa que pida al usuario que introduzca una frase en 
#la consola y muestre por pantalla la frase invertida.
 
Frase = input("Introduzaca una frase: ")

# Invertir la frase utilizando slicing
frase_invertida = Frase[::-1]


print(F'la frase invertida es {frase_invertida}')

