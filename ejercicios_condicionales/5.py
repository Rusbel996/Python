#Para tributar un determinado impuesto se debe ser mayor de 16 años y 
#tener unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos 
#mensuales y muestre por pantalla si el usuario tiene que tributar o no.

Edad = int(input("Cual es su edad: "))

Ingresos = float(input("Cuales so sus ingresos: "))


#Veremos si tributa 

if Edad  > 16 and Ingresos >= 1000:
    print("Si puede tributar")
    
else : 
    print("No puede tributar")    