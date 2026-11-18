def mostrar_menu() -> None:
    print("""
    1. Añadir un elemento a la lista.
    2. Cambiar el valor de un elemento de la lista.
    3. Eliminar un elemento de la lista.
    4. Eliminar todos los elementos de la lista.
    5. Mostrar los elementos de la lista.
    0. Salir del programa.
    """)


def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('El valor introducido no es un número válido.')


def anyadir_elemento() -> None:
    elem = input('Introduzca el elemento a añadir: ')
    lista.append(elem)


def mostrar_lista() -> None:
    print(lista)


def cambiar_elemento() -> None:
    mostrar_lista()
    indice = pedir_entero('Introduzca el índice del elemento a cambiar: ')
    valor = input('Introduzca el nuevo valor del elemento: ')
    try:
        lista[indice] = valor
    except IndexError:
        print('El índice no está dentro de los límites de la lista.')


def eliminar_elemento() -> None:
    mostrar_lista()
    indice = pedir_entero('Introduzca el índice del elemento a borrar: ')
    try:
        del lista[indice]
    except IndexError:
        print('El índice no está dentro de los límites de la lista.')


def eliminar_todos() -> None:
    lista.clear()


lista: list[str] = []

while True:
    mostrar_menu()
    opc = input('Introduzca la opción deseada: ')
    match opc:
        case '0':
            break
        
        case '1':
            anyadir_elemento()

        case '2':
            cambiar_elemento()

        case '3':
            eliminar_elemento()

        case '4':
            eliminar_todos()

        case '5':
            mostrar_lista()

