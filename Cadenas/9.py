#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior 
#para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

Fecha_Nacimiento = input("Introduce tu fecha de nacimiento en este formato dd/mm/aaa: ")


Dia , mes , año = Fecha_Nacimiento.split('/')

print(f'tu fecha den nacimiento es dia {Dia} mes {mes} y año {año}')
