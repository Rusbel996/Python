#En una determinada empresa, sus empleados son evaluados al final de cada año
#3. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
#traduciéndose en mejores beneficios. Los puntos que pueden conseguir
#los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
#A continuación se muestra una tabla 
#con los niveles correspondientes a cada puntuación. La cantidad de dinero 
#conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.


Puntuacion = float(input("Cual es la puntuacion del usuario: "))


niveles = {
    
    0.0: "Inaceptable",
    0.4: "Aceptable",
    0.6: "Meritorio"  
}

if Puntuacion in niveles:

  cantidad_dinero = 2400 * Puntuacion
  
  print(f'Tu puntiacion es {niveles[Puntuacion]} y la cantidad de dinero es {cantidad_dinero}')
  
else :
    print("La puntuacion ingresada no es valida ")  


