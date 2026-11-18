"""
8. Escribir un programa que calcule la media de cinco valores
numéricos reales (tipo float) introducidos por teclado.
"""

CUANTOS = 5   # ¿A cuántos valores le queremos calcular la media?

lista: list[float] = []

while len(lista) < CUANTOS:
    try:
        valor = float(input('Introduzca un número real: '))
        lista.append(valor)
    except ValueError:
        print('Ha introducido un valor incorrecto.')

media: float = sum(lista) / len(lista)
print('La media es:', media)
