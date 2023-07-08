def solve_labyrinth(labyrinth):

    # Obtener las dimensiones del laberinto
    rows = len(labyrinth)
    cols = len(labyrinth[0])

    # Crear una matriz para rastrear los caminos visitados y las distancias
    visited = []
    for _ in range(rows):
        row_col = []
        for _ in range(cols):
            row_col.append(False)
        visited.append(row_col)

    distances = []
    for _ in range(rows):
        row_col = []
        for _ in range(cols):
            row_col.append(-1)
        distances.append(row_col)


    # Definir las direcciones de movimiento (arriba, abajo, izquierda, derecha)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Cola para el algoritmo 
    movement = []

    # Agregar la posición de inicio a la cola
    movement.append((0, 0))
    visited[0][0] = True
    distances[0][0] = 0

    # Búsqueda 
    while movement:
        row, col = movement.pop(0)

        # Verificar si hemos alcanzado la meta (esquina inferior derecha)
        if row == rows-1 and col == cols - 1:
            return distances[row][col]

        # Explorar las celdas vecinas
        for drow, dcol in directions:
            new_row, new_col = row + drow, col + dcol

            # Verificar si la celda vecina está dentro de los límites del laberinto
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Verificar si la celda vecina no es una pared y no ha sido visitada
                if labyrinth[new_row][new_col] == "." and visited[new_row][new_col] == False:

                    # Marcar la celda vecina como visitada
                    visited[new_row][new_col] = True

                    # Calcular la distancia a la celda vecina
                    distances[new_row][new_col] = distances[row][col] + 1

                    # Agregar la celda vecina a la cola
                    movement.append((new_row, new_col))

    # Si no se encontró una ruta válida, retornar -1
    return -1


# Ejemplo 1
labyrinth =   [[".",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".",".","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","."]]



min_moves_1 = solve_labyrinth(labyrinth)
if min_moves_1 == -1:
    print("-1")
else:
    print("Número mínimo de movimientos ejercicio 1:", min_moves_1)

# Ejemplo 2
labyrinth =  [[".",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".","#","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","."]]


min_moves_2 = solve_labyrinth(labyrinth)
if min_moves_2 == -1:
    print("-1")
else:
    print("Número mínimo de movimientos ejercicio 2:", min_moves_2)

# Ejemplo 3
labyrinth =  [[".",".","."],
[".",".","."],
[".",".","."]]


min_moves_3 = solve_labyrinth(labyrinth)
if min_moves_3 == -1:
    print("-1")
else:
    print("Número mínimo de movimientos ejercicio 3:", min_moves_3)

# Ejemplo 4
labyrinth = [[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".","#",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".","#",".",".",".","#",".",".",".","."],
[".",".",".",".",".",".","#",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."]]


min_moves_4 = solve_labyrinth(labyrinth)
if min_moves_4 == -1:
    print("-1")
else:
    print("Número mínimo de movimientos ejercicio 4:", min_moves_4)