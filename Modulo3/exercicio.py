l1 = [[1,2,3],[1,1,2,3,4],[4,5,3,2,3,4]]

"""
- percorrer a lista de listas
- percorrer cada lista
- buscar o segundo numero de uma duplicação, ex.: 1,2,2,3 = {2}
- se não encontrar duplicados, devolver -1

"""

"""
para listas em Lista:
    
"""

l1 = list(l1)

n1, n2, n3 = l1

# n1 = set(n1)
# n2 = set(n2)
# n3 = set(n3)

duplicado = set()

# print(n1)
# print(n2)
# print(n3)

for valor in n1:
    if valor:
        duplicado = valor
        print(duplicado)

print()


def encontrar_duplicado(param_n2):
    duplicado2 = set()
    dup = -1

    for valor in param_n2:
        if valor in duplicado2:
            dup = valor
            break

        duplicado2.add(valor)
    
    return dup

for item in l1:
    print(item, encontrar_duplicado(item))