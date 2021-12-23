"""
Desafio de Contadores

Na estrutura de repetição, criar 2 contadores onde em cada volta
um contador conte de forma progressiva e o outro de forma
regressiva

"""

i = 0
j = 10

while i < 10 and j > 1:
    print(i, j)
    i += 1
    j -= 1
    if i > 8:
        break

"""
Resolução do professor:
"""

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
