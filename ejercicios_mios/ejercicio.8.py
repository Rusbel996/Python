#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
#el número de años, y muestre por pantalla el capital obtenido en la inversión.


inversion = float(input("Cual es el capital a invertir: "))

interes_anual = float(input("Cual es el interes anual: "))

años = float(input("Cual es la cantidad de años: "))


# Capital = inversion // interes * tiempo 

Capital = inversion / (interes_anual * años)


print(f'el capital de la inversion es {Capital}')


# Solicitar al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
num_anios = int(input("Ingrese el número de años: "))

# Convertir el interés a la forma decimal
interes_decimal = interes_anual / 100

# Calcular el capital obtenido en la inversión utilizando la fórmula del interés compuesto
capital_obtenido = cantidad_invertir * (1 + interes_decimal)**num_anios

# Mostrar el resultado por pantalla
print(f"El capital obtenido después de {num_anios} años es: {capital_obtenido:.2f}")

