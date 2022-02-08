"""
split - Dividir uma string # str
join - Juntar uma lista # str
enumerate - Enumerar elementos da lista # iteráveis
"""

string = 'O Brasil é o país do futebol'

lista = string.split(' ')  # separa cada palavra da frase, indexa cada uma em um indice le uma lista = ['O', 'Brasil', 'é', 'o', 'país', 'do', 'futebol']
string2 = ' *-* '.join(lista)  # junta os elementos de uma lista especificada dentro de (), e os separa com o elemento separador especificado dento de ' '.<antes do join>
print('essa é só uma string = {0}\nnessa foi usado split e virou lista = {1}\nnessa juntou a string com a string2 com o join e separou-as com *-* = {2}\n'.format(string,lista,string2))

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

lista1 = [
    ['edu', 'helena', 'samuel'],
    ['elen', 'julia', 'pearl']
]

enumerada = list(enumerate(lista1))
                             #  0, 1 = indices_da_lista_de_listas
print('\n',enumerada)  # [(0, ['edu', 'helena', 'samuel']), (1, ['elen', 'julia', 'pearl'])]
                             #      '------ elementos da lista com indices próprios 0, 1, 2 ---'
print(enumerada[1][1])


