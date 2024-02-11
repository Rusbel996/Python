#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso  = 1.5

#Duracion de crudos 

crudo_promedio = 5
crudo_dalto =  3.5




#Diferencia de duaracion 

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacio removido

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 100 // otros_cursos_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#Monstrando las diferencias de duracion (ejercicio A)
print(f'el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'el curso de dalto dura un {diferencia_con_max}% menos que el mas rapido')
print(f'el curso de dalto dura un {diferencia_con_promedio}% menos que el mas rapido')


#Monstrando la cantidad  de espacio vacios que se remueven 

print(f'el curso de promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'el curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')

#Monstrando diferencias si los cursos durara 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso') 


