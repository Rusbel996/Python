frutas = ["banana", "manzana","ciruela", "pera","naranja","granada","durazno"]
cadena = "Hola Dalto"
numeros = [2,5,8,10]

#evitando que se coma una manzan con la sentencia continue 

for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f'me voy a comer {fruta}')
    
#recorrer una cadena de texto 
for letra in cadena:
    print(letra)


#for en una sola linea de codigo

numero_duplicados = list()

for numero in numeros:
    numero_duplicados.append(numero*2)
    
print(numero_duplicados)        
    

#evitar que el bucle siga ejecutandose 

for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera' :
        break
else:
     print("terminado")   

#for en uan sola linea de codigo (duplicamos los numeros)

numeros_duplicados = [x*2 for x in numeros]

print(numero_duplicados)

   