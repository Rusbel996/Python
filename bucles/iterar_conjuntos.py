animales = {"gato","perro","loro","cocodrilo"}
numeros = {52,16,14,72}

#recorriendo la conjunto animales

for animal in animales: 
    
    print(f'Ahora la variable animal es igual a: {animal}')    
    
#recorriendo la conjunto numeros y multiplicando cada valor por 10

for numero in numeros:
        resultado = numero *  20
        print(resultado)
        
        
 #iterando dos conjuntos del mismo tamaño al mismo tiempo       
for numero,animal in zip(animales,numeros):
    print(f"recorriendo conjunto 1: {numero}")
    print(f"recorriendo conjunto 2: {animal}")        
    
    

#forma correcta de recorrer una conjunto con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

    
#usando el else 

for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}') 
else:
    print("el bucle termino")       