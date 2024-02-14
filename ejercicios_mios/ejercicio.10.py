#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de 
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año,
#se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la
#cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa 
#debe calcular y mostrar por pantalla la cantidad de ahorros tras 
#el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

cantidad_inicial = float(input("Ingrese la cantidad de dinero depositado: "))

tasa_interes_anual = 0.04

#Calculando el saldo final despues del primer año

# Calcular el saldo final después del primer año
saldo_1 = cantidad_inicial * (1 + tasa_interes_anual)

# Calcular el saldo final después del segundo año
saldo_2 = saldo_1 * (1 + tasa_interes_anual)

# Calcular el saldo final después del tercer año
saldo_3 = saldo_2 * (1 + tasa_interes_anual)

# Mostrar el saldo final después de cada año, redondeado a dos decimales
print(f"Saldo después del primer año: {saldo_1:.2f}")
print(f"Saldo después del segundo año: {saldo_2:.2f}")
print(f"Saldo después del tercer año: {saldo_3:.2f}")