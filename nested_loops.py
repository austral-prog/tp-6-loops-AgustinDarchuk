# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []
    for i in matrix:
        for a, element in enumerate(i):
            lista.append(element)
        
    return lista

# print(flatten([[1, 2], [3, 4], [5, 6]]) )

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    
    suma = 0
    
    lista = []
    for i in matrix:
        for a in i:
             suma = suma + a
        lista.append(suma)
        suma = 0
    return lista
    
# print(row_sums([[1, 2, 3], [4, 5, 6]]))


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    cantidad_filas = len(matrix[0])
    lista = []
    
    for elemento in range(cantidad_filas):
        
        suma = 0
        
        for i in matrix:
            suma = suma + i[elemento]
    
        lista.append(suma)
        
    return lista

# print(col_sums([[1, 2, 3], [4, 5, 6]]))