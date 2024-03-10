#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
#posterior a la N y el grupo B por el resto. 
#Escribir un programa que pregunte al usuario su nombre y sexo, 
#y muestre por pantalla el grupo que le corresponde.

Nombre = input("Cual es su nombre: ")

Sexo = input("Cual su sexo F o M: ")

#Convertir el nombre a minusculas para comparaciones mas faciles 

nombre_minus = Nombre.lower()


#En este caso específico, nombre < "m" compara el nombre ingresado por el 
#usuario con la letra "m". Si el nombre del usuario es alfabéticamente 
#anterior a "m" en orden lexicográfico, la expresión nombre < "m" será verdadera y 
#se ejecutará el primer segmento de la condición en el if.

#Determinar el grupo al que pertenece el usuario

if (Sexo == "F" and nombre_minus < "m" ) or (Sexo == "M" and nombre_minus > "n"):
    grupo = "A"
    
else:
    grupo = "B"
    
#Mostrar por pantalla el grupo al que pertene el usuario


print(f'Tu nombre es {nombre_minus.capitalize()} y perteneces al grupo {grupo}')        
