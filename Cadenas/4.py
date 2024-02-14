#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
#es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
#Escribir un programa que pregunte por un número de teléfono con este
#formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.



# Solicitar al usuario el número de teléfono con el formato prefijo-número-extension
telefono = input("Ingrese el número de teléfono con el formato +34-número-extension: ")
#Como ingreamos el numero +51-944441609-67

# Separar el número de teléfono en prefijo, número y extensión
partes_telefono = telefono.split("-")

# Extraer el número de teléfono sin el prefijo y la extensión
numero_sin_prefijo_extension = partes_telefono[1]
#al nomento de separar los elementos coo prefijo y extension 
#--0--1--2----
#+51-944441609-67



# Imprimir el número de teléfono sin el prefijo y la extensión
print("Número de teléfono sin prefijo y extensión:", numero_sin_prefijo_extension)