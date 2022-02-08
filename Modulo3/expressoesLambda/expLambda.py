"""
Expressões LAMBDA são funções anônimas
por exemplo:
eu posso ter uma lista onde:
lista = [[a=1], [b=2], [c=3]]

Se eu quiser ordenar ou alterar essa lista, com funções comuns, eu precisaria percorrer
com um for, usar talvez If's...
enquanto que com expressões LAMBDA, é possivel simplifcar
"""

lista = [
    ['a', 15],
    ['b', 6],
    ['c', 22]
]

# para ordenar com exp. lambda, é só:

print(sorted(lista, key=lambda i: i[1]))  # i[1] é item nas listas no index 1 = numeros (6, 15, 22)
# output = [[a=1], [b=2], [c=3]]

