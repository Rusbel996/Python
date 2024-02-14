#Escribir un programa que pregunte el nombre completo del 
#usuario en la consola y después muestre por pantalla el nombre 
#completo del usuario tres veces, una con todas las letras minúsculas,
#otra con todas las letras mayúsculas y otra solo con la primera letra del
#nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre 
#combinando mayúsculas y minúsculas como quiera.


Nombre = input("Cual es tu nombre completo xd: ")

Mayuscula = Nombre.upper()

Minuscula = Nombre.lower()

Primera_Mayuscula = Nombre.capitalize()

print((Nombre + "\n") * int(3))

print(f'Nombre en mayuscula {Mayuscula}')

print(f'Nombre en minuscula {Minuscula}')

print(f'Nombre con solo la primera letra en mayuscula {Primera_Mayuscula}')

print(Nombre.title())



