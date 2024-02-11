#Enunciado 

#Se tarda 1 segunbdo en decir 2 palabras 
#¿Cuantos segundos se tarda en decir X palabras ?

#A)Pedirle al usuario que diga 
#cualquier texto real y:   
#-calcular cuanto tardaria en decir esa frase 
#¿Cuantas palabras dijo?

#B) si se tarda mas de 1 minuto_:
#    _ decirle: "para flaco tammpoco te pedi un testamento".hp

#C) Dalto habla un 30% mas rapido:
#¿Cuanto  tardaria el en decirlo?
    

dime_texto = input("Decime un texto y te dijo cuanto tiempo tardas en decirlo: ")

palabras_separadas = dime_texto.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f'Dijiste {cantidad_de_palabras} palabras , y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diria {cantidad_de_palabras/2*1.3} segundos en decirlo')
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi a jorge")



   