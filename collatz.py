

def collatz_steps(n):
    """
    Retorna la cantidad de pasos necesarios para llegar a 1
    siguiendo la conjetura de Collatz:
      - Si n es par: n = n // 2
      - Si n es impar: n = 3 * n + 1

    n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

    Ejemplo: collatz_steps(6) -> 8
      6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
    """
    counter = 0
    while n > 1:
      if n % 2 == 0:
        n = n/2
        counter += 1
      elif n % 2 == 1:
        n = n*3 + 1
        counter += 1
      elif n == 1:
        n = n * 3 + 1
        counter +=1
    return counter

# print(collatz_steps(10))

def collatz_sequence(n):
    """
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    
    lista = []
    lista.append(n)
    while n > 1:
      if n % 2 == 0:
        n = n/2
        lista.append(int(n))
      elif n % 2 == 1:
        n = n*3 + 1
        lista.append(int(n))
      elif n == 1:
        lista.append(int(n))
    return lista

# print(collatz_sequence(6))
