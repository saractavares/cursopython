"""
elementos da tupla são imutáveis
"""
tupla1 = (1, 2, 3, 'Sara', '123')  # tuplas ficam entre parênteses

print(type(tupla1))  # output : <class 'tuple'>
print(tupla1)
print(tupla1[2], '  - terceiro print')

for i in tupla1:
    print(i)


tupla2 = 1, 2, 3,  # assim tbm é tupla, sem os parênteses

print(type(tupla2))

tupla3 = tupla1+tupla2

print(tupla3)  # (1, 2, 3, 'Sara', '123', 1, 2, 3)

n1, n2, n3, *n, ultimo = tupla3

print(*n)  # Sara 123 1 2

# Editar tupla:

tupla1 = list(tupla1)  # agora a tupla é lista e pode ser modificada

print(tupla1)  # [1, 2, 3, 'Sara', '123']

tupla1[-1] = 80

# Voltando a ser tupla:

tupla1 = tuple(tupla1)

print(tupla1)
