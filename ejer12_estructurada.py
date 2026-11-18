
lista = []

while True:
    print("""
    1. Añadir un elemento a la lista.
    2. Cambiar el valor de un elemento de la lista.
    3. Eliminar un elemento de la lista.
    4. Eliminar todos los elementos de la lista.
    5. Mostrar los elementos de la lista.
    0. Salir del programa.
    """)

    opcion = input('Introduzca la opción deseada: ')

    match opcion:
        case '0':
            print('Adiós')
            break
    
        case '1':
            elem = input('Introduzca el elemento a añadir: ')
            lista.append(elem)
        
        case '2':
            try:
                indice = int(input('Introduzca el índice del elemento a cambiar: '))
                nuevo = input('Introduzca el nuevo valor: ')
                lista[indice] = nuevo
            except ValueError:
                print('Ha introducido un índice no numérico.')
            except IndexError:
                print('Ese índice no existe en la lista.')
        
        case '5':
            print(lista)
            
        case _:
            print('Opción incorrecta.')
