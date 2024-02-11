#creando diicionarios con dict()

diccionario = dict(nombre="Lucas", apellidos= "dalto")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos 
diccionario = {frozenset(["dalto","rancio"]): "jajaas"}

#creando diccionarios con fromkeys()

diccionario = dict.fromkeys(["nomnbre","apellido", "suscriptores"])

print(diccionario["apellido"])