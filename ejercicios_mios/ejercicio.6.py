#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, y
#muestre por pantalla la frase Tu índice de masa corporal 
#es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.



Peso = float(input("Cual es su peso obeso: "))
Estatura = float(input("Cual es su estatura: "))


IMC = round((Peso / (Estatura**2)),2)

if IMC > 25:
    print(f'Usted esta en sobrepeso {IMC}')

else:
   print(f'usted esta bien {IMC}')



#print(f'este es tu indice de masa corporal {IMC}')