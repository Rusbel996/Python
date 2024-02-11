diiccionario = {
    "nombre" : 'lucas',
    "apellido" : 'dalto',
    "subs" : 10000000
}

#nos devuelve un objeto dict_item
claves = diiccionario.keys()

valor_de_kasdks = diiccionario.get("kasdks")
print("hola papa, el programa continua")

#eliminando todo el diccioanario 
#diiccionario.clear()

#eliminando un elemento del diccionario
diiccionario.pop("subs")

#obteniendo un elemento dict_items iterable

diiccionario_iterable = diiccionario.items()


print(claves)