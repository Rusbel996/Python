cadena1 = "Hola,soy,Dalto,hola"
cadena2 = "Bienvenido maquinola"

#convierte a mayusculas 

mayusc = cadena1.upper()

#convierte a minusculas

minus = cadena2.lower()

#primera letra en mayuscula

primer_letra_mayusc = cadena1.capitalize()


#buscamos una cadena en  otra cadena , si no hay coindencias devuelve -1

busqueda_find = cadena1.find("H")

#buscamos una cadena en otra cadena , si no hay coincidencias lanza una expecion
#busqueda_index = cadena1.index("a")


#si es numerico, devolvemos true, sino devolvemos false

es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true , sino devolvemos false

es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("hola")


#contamos cuantos caracteres tiene una cadena
#len no es un metodo , es una funcion
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada , si es asi devuelve True
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada , si es asi devuelve True

termina_con = cadena1.endswith("a")

#si el valor 1 , se encuentra en la cadena original , remplaza el valor 1 de la misma , por el valor 2
cadena_nueva = cadena1.replace(",","gaaa")
cadena_nueva_2 = cadena_nueva.capitalize()


#separar cadenas con la cadena que le pasemos
cadena_nueva = cadena1.split(",")

print(contar_caracteres)
print(empieza_con)
print(termina_con)
print(cadena_nueva)
print(cadena_nueva_2)
print(cadena_nueva)