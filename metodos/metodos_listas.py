#Creando una lista con list()

lista = list([34,56,23,True])

#devuelve la cantidad de elementos de la lista

cantidad_elementos = len(lista)

#agregando un elemento a la lista

lista.append(6)

#agregando un elemento a la lista en un indice especifico

lista.insert(2,34)

#agregando varios elementos a la lista

lista.extend([2030])


#eliminando un elemento de la lista (por su indice)

lista.pop(3) #-1 para eliminar el ultimo ,-2 para eliminar al antepenultimo , de los nuevos elementos agregados 


#removiendo un elemento  de la lista por su valor

#lista.remove("Toma jorge")


#ordenando la lista de forma ascendentes (si usamos el parametri reverse= True lo ordena en reversa)

lista.sort()


#inviertiendo los elementos de una lista

lista.reverse()


#verificando si un elemento se encuentra en la lista

elemento_encontrado = lista.index(56)


print(lista)
print(elemento_encontrado)