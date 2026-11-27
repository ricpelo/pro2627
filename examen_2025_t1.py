from typing import Any

def colapsar(lista: list[tuple[Any, int]]) -> list[Any]:
    """
    Devuelve una lista que contiene elementos repetidos según se
    especifica en las tuplas de la lista original.
    
    Debe recibir una lista de tuplas de la forma (valor, cantidad) y
    devolver una nueva lista que contenga _cantidad_ copias del _valor_
    original.

    >>> colapsar([(7, 3), (2, 1)])
    [7, 7, 7, 2]
    >>> colapsar([(1, 1), (2, 2), (3, 3)])
    [1, 2, 2, 3, 3, 3]
    >>> colapsar([])
    []
    """
    i = 0
    res = []
    while i < len(lista):
        elem, cant = lista[i]
        res += [elem] * cant
        i += 1
    return res


def compresion_simple(lista: list[Any]) -> list[tuple[Any, int]]:
    """
    Comprime los elementos repetidos de una lista de enteros.
    
    Devuelve una lista donde las repeticiones consecutivas son
    sustituidas por tuplas de la forma (valor, cantidad).
    
    >>> compresion_simple([1, 1, 1, 2, 2, 1, 3])
    [(1, 3), (2, 2), (1, 1), (3, 1)]
    >>> compresion_simple([])
    []
    """
    res = []
    i = 0
    while i < len(lista):
        elem, cant = lista[i], 0
        while i < len(lista) and lista[i] == elem:
            cant += 1
            i += 1
        res.append((elem, cant))
    return res


def normalizar_nombres(nombres: list[str]) -> list[str]:
    """
    Normaliza nombres.
    
    Recibe una lista de cadenas con posibles espacios extra y que
    mezcla incorrectamente mayúsculas y minúsculas, y devuelve una
    una lista con los nombres normalizados:
    
    - Elimina espacios iniciales y finales.
    - Sustituye varios espacios internos consecutivos por uno solo.
    - Pone la inicial de cada palabra en mayúsculas y el resto en
      minúsculas.
      
    >>> normalizar_nombres(["   ana    LópEz ", "JOSÉ    PÉREZ  "])
    ['Ana López', 'José Pérez']
    """
    def limpiar(nombre: str) -> str:
        return " ".join(nombre.title().strip().split())
    res = []
    i = 0
    while i < len(nombres):
        res.append(limpiar(nombres[i]))
        i += 1
    return res


def intercalar(a: list, b: list) -> list:
    """
    Devuelve una lista con los elementos de a y b intercalados.

    Si una lista es más larga que la otra, los elementos sobrantes
    se añaden al final.
    
    >>> intercalar([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> intercalar([1, 3], [2, 4, 6])
    [1, 2, 3, 4, 6]
    """
    res = []
    n = min(len(a), len(b))
    i = 0
    while i < n:
        res.append(a[i])
        res.append(b[i])
        i += 1
    res += a[i:]
    res += b[i:]
    return res


def analizar_secuencias(lista: list[list[int]]) -> list[tuple[int, int, int]]:
    """
    Calcula, para cada sublista, la longitud, la suma y el máximo.

    >>> analizar_secuencias([[1, 2, 3], [5, 1]])
    [(3, 6, 3), (2, 6, 5)]
    """
    











def test_colapsar1():
    assert colapsar([(7, 3), (2, 1)]) == [7, 7, 7, 2]

def test_colapsar2():
    assert colapsar([(1, 1), (2, 2), (3, 3)]) == [1, 2, 2, 3, 3, 3]

def test_colapsar3():
    assert colapsar([]) == []
