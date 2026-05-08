

def put(value, lst):
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    
    for i, element in enumerate(lst):
        if element == "":
            lst[i]= value
            return i     
    return -1


# print(put("Blue", ["Red", "Green", "", "", "Pink", "", "Black"]))

def remove(value, lst):
    """
    Busca todas las ocurrencias de value en lst, las reemplaza por ""
    y retorna la cantidad de eliminaciones realizadas.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "Green", "Red", "Blue"]
        remove("Red", colors) -> 2
        # colors ahora es ["", "Green", "", "Blue"]
    """
    errasements = 0 
    for i, element in enumerate(lst):
        if element == value:
            lst[i]= ""
            errasements += 1
    return errasements


# print(remove("Blue", ["Red", "Green", "White"]))
