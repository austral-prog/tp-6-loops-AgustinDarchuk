# Replace the "ANSWER HERE" for your answer

def find_min(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el menor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_min([3, 1, 7, 2]) -> 1
    Ejemplo: find_min([5, 5, 5]) -> 5
    Ejemplo: find_min([-3, -1, -7]) -> -7
    """
    
    lista = []
    
    for element in numbers:
        if lista == []:
            lista.append(element)
        else:
            if element < lista[0]:
                lista[0] = element
    
    return lista[0]

# print(find_min([-3, -1, -7]))

def find_max(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el mayor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_max([3, 1, 7, 2]) -> 7
    Ejemplo: find_max([5, 5, 5]) -> 5
    Ejemplo: find_max([-3, -1, -7]) -> -1
    """
    
    lista = []
    
    for element in numbers:
        if lista == []:
            lista.append(element)
        else:
            if element > lista[0]:
                lista[0] = element
    
    return lista[0]


# print(find_max([3, 1, 7, 2]))

def count_negatives(numbers):
    """
    Dada una lista de numeros, retorna la cantidad de numeros negativos.
    Si la lista esta vacia, retorna 0.

    Ejemplo: count_negatives([3, -1, -7, 2]) -> 2
    Ejemplo: count_negatives([1, 2, 3]) -> 0
    Ejemplo: count_negatives([-1, -2, -3]) -> 3
    """
    

    negatives = 0  
    for i in numbers:
        if i < 0:
            negatives = negatives + 1
    return negatives

# print(count_negatives([-1, -2, -3, -2, 1, 6]))