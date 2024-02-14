#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.


Numero_Horas = float(input("Cual es el numero de horas que trabajas burro: "))

Costo_Hora = float(input("cuanto te pagan por la hora de trabajo: "))


Sueldo = Numero_Horas * Costo_Hora

print(f'Este es tu pago {Sueldo}')