"""
- listas 
- fatiamento
- append, insert, pop, del, clear, extend, +
- min, max
- range
"""

# texto = 'Valor'  # variável com apenas 1 valor
# lista = [1, 2, 3, 4]  # variável com vários valores


""" ACESSANDO VALORES DA LISTA PELO INDEX
#         0    1    2    3    4   
lista = ['a', 'b', 'crocodilo', 'd', 'e']

string = 'ABCDE'

print(string[2])

print(lista[2])
"""

""" FATIANDO VALORES DA LISTA

"""    # 0  1  2  3  4  5  6  7      8
lista = [1, 2, 3, 4, 5, 6, 7, 8, 'CARROSSEL']

print(lista, '\n #### lista completa\n')  # mostra a lista completa
print(lista[2:5], '\n #### apenas os valores do indice 2 - 4\n')  # mostra apenas os valores do indice 2 - 4 = '3, 4, 5'

lista2 = lista[4:8]  # recebe apenas os valores dos indices 4 - 7 = '5, 6, 7, 8'
print(lista2, '\n #### lista2 recebe apenas os valores dos indices 4 - 7\n')

lista.extend(lista2)  # junta à direita da lista os valores da lista2 = '[1, 2, 3, 4, 5, 6, 7, 8, 'CARROSSEL', 5, 6, 7, 8]
print(lista, '\n #### extend junta à direita da lista os valores da lista2\n')

lista2.pop()  # retira o último valor da lista2 = '8'
print(lista2, '\n #### pop retira o último valor da lista2 = "8"\n')

lista3 = ['a', 'b', 'c']
print(lista3, '\n #### lista3 completa\n')

lista.extend(lista3)
print(lista, '\n #### extend adicionou os valores de uma lista à outra\n')

lista4 = lista3 + lista2
print(lista4, '\n #### concatenou os valores da lista3 e lista2 para formar uma nova lista 4\n')

lista.append(lista4)
print(lista, '\n #### append adicionou a lista4 à lista\n')

last_ind = lista2[-1]  # buscando o ultimo indice da lista2
lista2.insert(last_ind, 8)  # inserindo valor 8 no último indice
print(lista2, '\n #### inserindo valor 8 no último indice\n')

del(lista[5])  # com del é possível deletar um valor de um indice especifico
print(lista, '\n #### lista com valor "6" deletado\n')  

#########################

# min & max

print(min(lista2), '\n #### menor valor da lista2\n')  # traz o menor valor da lista
print(max(lista2), '\n #### maior valor da lista2\n')  # traz o maior valor da lista


