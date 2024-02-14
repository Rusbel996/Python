#Escribir un programa que pregunte el nombre del usuario en la consola y
#después de que el usuario lo introduzca muestre por 
#pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de 
#usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


Nombre = input("Cual es tu nombre: ")


Contar_letras = len(Nombre)

print(f'Este es el nombre {Nombre} y la cantidad de letras es {Contar_letras}')


