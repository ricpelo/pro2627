"""
8. Escribir un programa que calcule la media de cinco valores
numéricos reales (tipo float) introducidos por teclado.
"""

CUANTOS = 5   # ¿A cuántos valores le queremos calcular la media?
i: int = 0
suma: float = 0

while i < CUANTOS:
    try:
        suma += float(input('Introduzca un número real: '))
        i += 1
    except ValueError:
        print('Ha introducido un valor incorrecto.')

media: float = suma / CUANTOS
print('La media es:', media)
