# un programa que pida al usuario un número entero positivo y muestre por pantalla
#la cuenta atrás desde ese número hasta cero separados por comas.


#El bucle for que has mencionado se construye con la función range(), que genera una secuencia de números enteros. La sintaxis general de range() es la siguiente: range(start, stop, step).

#start: El primer número en la secuencia (por defecto es 0).
#stop: El final de la secuencia (no incluido).
#step: El tamaño del paso entre cada número en la secuencia (por defecto es 1).
#En el caso específico que has mencionado: range(1, n+1, 2)

#start es 1, ya que queremos iniciar la secuencia desde el número 1.
#stop es n+1, donde n es el número entero positivo introducido por el usuario. Esto se debe a que range() genera una secuencia que llega hasta, pero no incluye, el número stop. Así que para incluir n en la secuencia, necesitamos poner n+1.
#step es 2, lo que significa que nos moveremos de 2 en 2 en la secuencia, de modo que solo obtendremos números impares.





Numero = int(input("Ingrese un numero entero positivo: "))

for i in range(Numero, -1, -1):
    print(i, end=", ")
