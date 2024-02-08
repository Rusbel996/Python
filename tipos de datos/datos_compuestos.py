#orden de la lista
#lista = [0,1,2,3]
#creando una lista se pueden modificar
lista = ["Lucas Dalto","Soy Dalto",True,1.96]
#creando una tupla no se pueden modificar
tupla = ["Lucas Dalto","Soy Dalto",True,1.96]
#se imprime de acuerdo al orden
print(lista[3])

#esto es valido para una lista 

lista[3] = "Maquinola"

#esto 

#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)

conjunto = {"Lucas Dalto", "Soy Dalto",True, 1.85, "Soy Dalto"}

#print(conjunto[3]) -> no puede acceder al elemento


#creando un diccionario (dict)

diccionario = {
      
      'nombre' : "Lucas Dalto",
      'canal' : "Soy Dalto" ,
      'esta_emocionado' : True,
      'altura' : 1.85,
      'dato_duplicado' : "Soy Dalto"
     
    
}

print(diccionario['altura'] +2)
print(lista[3])


