#creando una funcion de 3 parametros

def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keyword arguments
frase_resultante = frase(adjetivo= "capo" ,nombre = "Jorge" , apellido = "Dalto")
print(frase_resultante)


#------------------------------------------------------------

def frase(nombre,apellido,adjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("Lucas","Dalto","inteligente")

print(frase_resultante)

