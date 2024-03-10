#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta = int(input("Cual es su renta  anual: "))


if Renta < 10000 :
    
    print("el tipo de tasa impositiva es 5%")
    
elif   10000 < Renta < 20000 : 
    print("el tipo de tasa impositivo es 15%")
    
    
elif  20000 < Renta < 35000  : 
    print("el tipo de tasa impositivo es 20%")
    
elif  35000 < Renta < 60000 :
    print("el tipo de tasa impositiva es 30%")
    
else :
  print("El tipo de tasa de impositiva es 45%")    
        
        
# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')        