#Escribir un programa que pregunte el correo electrónico del usuario en la 
#consola y muestre por pantalla otro correo electrónico con el 
#mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


Correo = input("Introduce tu correo electronico: ")

Correo_nuevo , Dominio = Correo.split('@')

Nuevo_Correo = Correo_nuevo + '@ceus.es'
print(f'El nuevo correo es {Nuevo_Correo}')