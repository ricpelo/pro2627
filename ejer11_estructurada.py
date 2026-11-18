"""
11. Escribir un programa que determine si un número entero
introducido por teclado es primo o compuesto.
(A partir del 2)
"""

n = int(input('Introduzca un número entero mayor o igual que 2: '))
i = 1
cuantos = 0    # Almacena la cantidad de divisores que tiene n

while i <= n:
    if n % i == 0:
        cuantos += 1
    i += 1

if cuantos == 2:
    print("Es primo")
else:
    print("Es compuesto")
