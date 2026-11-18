"""
14. Convertir una cantidad de tiempo (en segundos, Z)
en la correspondiente en horas, minutos y segundos, con
arreglo al siguiente formato:

3817 segundos = 1 horas, 3 minutos y 37 segundos
"""

try:
    total = int(input('Introduzca cantidad de tiempo en segundos: '))
    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(horas, 'horas,', minutos, 'minutos y', segundos, 'segundos')
except ValueError:
    print('Valor introducido incorrecto.')
