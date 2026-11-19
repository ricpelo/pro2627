def contar_numeros(lista: list[int]) -> tuple[int, int, int]:
    pos, neg, cero = 0, 0, 0
    i = 0
    while i < len(lista):
        if lista[i] > 0:
            pos += 1
        elif lista[i] < 0:
            neg += 1
        else:
            cero += 1
        i += 1
    return (pos, neg, cero)
    
    
print(contar_numeros([5, -3, 0, 8, -2, 0, 7])) # => (3, 2, 2)


def eliminar_repetidos(lista: list) -> list:
    ...
    
eliminar_repetidos([2, 4, 2, 6, 4, 8, 8, 10]) # => [2, 4, 6, 8, 10]

