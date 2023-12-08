'''
imprime los elementos de la fila separados por un espacio'''
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

'''
esta función hace que se cree un tablero de ajedrez en el que las piezas se encuentran en su posicion inicial.'''
def crear_tablero():
    # Crear un tablero vacío de 8x8 utilizando una lista de listas. 
    # Cada elemento en el tablero inicialmente es un espacio en blanco.
    tablero = [[" " for _ in range(8)] for _ in range(8)]

    # Configurar piezas en la posición inicial
    piezas_blancas = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
    piezas_negras= ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]

    # Configurar las filas de peones
    tablero[1] = ["♙" for _ in range(8)]
    tablero[6] = ["♟" for _ in range(8)]

    '''
    Se crea un bucle que posiciona las piezas en el orden dado de la lista en la primera y ultima fila. '''
    for i, pieza in enumerate(piezas_blancas):
        tablero[0][i] = pieza  # Fila superior (blancas)
        tablero[7][i] = piezas_negras[i] # Fila inferior (negras)

    return tablero

'''
creamos una lista de movimientos validos que restringen a la piezas dependiendo de sus posiciones'''
def es_movimiento_valido(tablero, fila_origen, columna_origen, fila_destino, columna_destino):
    # Verificar que las coordenadas estén dentro del rango del tablero
    if not (0 <= fila_origen < 8 and 0 <= columna_origen < 8 and 0 <= fila_destino < 8 and 0 <= columna_destino < 8):
        return False

    # Verificar que la pieza en la posición de origen sea válida
    pieza = tablero[fila_origen][columna_origen]
    if pieza == " ":
        return False

    # Verificar movimiento específico para cada tipo de pieza
    if pieza == "♙":  # Peón blanco
        # Movimiento básico del peón (avanzar una casilla hacia adelante)
        if fila_destino == fila_origen + 1 and columna_destino == columna_origen and tablero[fila_destino][columna_destino] == " ":
            return True
        # Primer movimiento del peón (avanzar dos casillas hacia adelante)
        elif fila_destino == fila_origen + 2 and columna_destino == columna_origen and fila_origen == 1 and tablero[fila_destino][columna_destino] == " ":
            return True
        # Captura diagonal del peón
        elif fila_destino == fila_origen + 1 and abs(columna_destino - columna_origen) == 1 and tablero[fila_destino][columna_destino].islower():
            return True
        else:
            return False

    elif pieza == "♟":  # Peón negro
        # Movimiento básico del peón (avanzar una casilla hacia adelante)
        if fila_destino == fila_origen - 1 and columna_destino == columna_origen and tablero[fila_destino][columna_destino] == " ":
            return True
        # Primer movimiento del peón (avanzar dos casillas hacia adelante)
        elif fila_destino == fila_origen - 2 and columna_destino == columna_origen and fila_origen == 6 and tablero[fila_destino][columna_destino] == " ":
            return True
        # Captura diagonal del peón
        elif fila_destino == fila_origen - 1 and abs(columna_destino - columna_origen) == 1 and tablero[fila_destino][columna_destino].isupper():
            return True
        else:
            print("Error: Movimiento no válido para el peón negro.")
            return False

    elif pieza == "♖":  # Torre
        # Movimiento horizontal o vertical
        if fila_origen == fila_destino or columna_origen == columna_destino:
            return True
        else:
            print("Error: Movimiento no válido para la torre.")
            return False

    elif pieza == "♘":  # Caballo
        # Movimiento en "L"
        delta_filas = abs(fila_destino - fila_origen)
        delta_columnas = abs(columna_destino - columna_origen)
        if (delta_filas == 2 and delta_columnas == 1) or (delta_filas == 1 and delta_columnas == 2):
            return True
        else:
            print("Error: Movimiento no válido para el caballo.")
            return False

    elif pieza == "♗":  # Alfil
        # Movimiento en diagonal
        delta_filas = abs(fila_destino - fila_origen)
        delta_columnas = abs(columna_destino - columna_origen)
        if delta_filas == delta_columnas:
        # Verificar que no haya piezas en el camino
            paso_filas = 1 if fila_destino > fila_origen else -1
            paso_columnas = 1 if columna_destino > columna_origen else -1

            for i in range(1, delta_filas):
                fila_intermedia = fila_origen + i * paso_filas
                columna_intermedia = columna_origen + i * paso_columnas
                if tablero[fila_intermedia][columna_intermedia] != " ":
                    print("Error: Movimiento no válido para el alfil.")
                return False

        return True
    else:
        print("Error: Movimiento no válido para el alfil.")
        return False   

'''
Ahora se crea una función que permita a las piezas moverse siempre que el movimiento sea válido.'''
def realizar_movimiento(tablero, fila_origen, columna_origen, fila_destino, columna_destino):
    pieza = tablero[fila_origen][columna_origen]

    while not es_movimiento_valido(tablero, fila_origen, columna_origen, fila_destino, columna_destino):
        print("Movimiento no válido. Inténtalo de nuevo.")
        imprimir_tablero(tablero)
        fila_origen = int(input("Ingresa la fila de la pieza a mover: "))
        columna_origen = int(input("Ingresa la columna de la pieza a mover: "))
        fila_destino = int(input("Ingresa la fila a la que mover la pieza: "))
        columna_destino = int(input("Ingresa la columna a la que mover la pieza: "))

    tablero[fila_origen][columna_origen] = " "
    tablero[fila_destino][columna_destino] = pieza
    return True



if __name__ == "__main__":
    tablero = crear_tablero()

'''
ahora se crea una opcion en la que el juego le preegunta al ususario si quiere jugar, que psicion tiene 
la pieza que quiere mover y a dónde la quiere mover.'''
while True:
        imprimir_tablero(tablero)

        opcion = input("¿Quieres hacer un movimiento? (s/n): ")
        
        if opcion.lower() != "s":
            break  # Terminar la partida si la opción no es 's'

        try:
            # Solicitar al usuario las coordenadas del movimiento
            fila_origen = int(input("Ingresa la fila de la pieza a mover: "))
            columna_origen = int(input("Ingresa la columna de la pieza a mover: "))
            fila_destino = int(input("Ingresa la fila a la que mover la pieza: "))
            columna_destino = int(input("Ingresa la columna a la que mover la pieza: "))

            # Realizar el movimiento en el tablero
            realizar_movimiento(tablero, fila_origen, columna_origen, fila_destino, columna_destino)
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")

# Guardar el tablero resultante al final del fichero
with open("partida-ajedrez.txt", "a") as archivo:
        for fila in tablero:
            archivo.write(" ".join(fila) + "\n")    
