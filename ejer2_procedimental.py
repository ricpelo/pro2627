def cuadrado(n: int) -> None:
    """Imprime un cuadrado con el número de líneas indicado."""
    i = 0
    while i < n:
        print('*' * n)
        i += 1


def cuadrado(n: int) -> None:
    def aux(filas: int) -> None:
        if filas == 0:
            return
        print('*' * n)
        aux(filas - 1)
    aux(n)


def diagonal(n: int) -> None:
    """Imprime una línea diagonal con el número de asteriscos indicado."""
    i = 1
    while i <= n:
        print(' ' * i, '*', sep='')
        i += 1
        
        
def arbol(n: int) -> None:
    """Imprime un árbol con la altura indicada."""
    if n == 0:
        return
    anchura = 2 * n - 1
    i = 1
    while i < n:
        cant_ast = 2 * i - 1
        print(('*' * cant_ast).center(anchura))
        i += 1
    print('*'.center(anchura))


"""
    ----*----         ---*---     --*--    -*-  *
    ---***---         --***--     -***-    -*-
    --*****--         -*****-     --*--
    -*******-         ---*---
    ----*----
"""    
    
    
    