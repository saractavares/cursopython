# """
# Formas de construir dicionários:
# """
# # d1 = {'chave1': 'valor da chave'}  # escrevendo cada chave e cada valor
# # d1 = dict(chave1='valor1', chave2='valor2')  # com a função dict
# # d1['nova_chave'] = 'nova_chave_valor'  # plotando valor no último index com colchetes

# d1 = {
#     'str': 'valor',
#     123: 'Outro valor',
#     (1, 2, 3): 'Tupla'
# }  # todos esses podem ser chaves em um dicionário

# """
# Formas de pegar um valor do dicionário pela chave:
# """

# # print(d1.get('str'))
# # print(d1.get(123))
# # print(d1.get((1, 2, 3)))
# # outputs =
# # valor
# # Outro valor
# # Tupla


# # d1['naoexiste'] = 'agora existe'

# # if 'naoexiste' in d1:
# #     print(d1['naoexiste'])
#       # output = 'agora existe'

# # d1['nomedachave'] = None

# # if d1.get('nomedachave') is not None:
# #     print(d1.get('nomedachave'))
# # else:
# #     print('a chave é None')

# # print(123)


# """
# Para mudar uma chave que já existe:
# """

# # d1.update({'nova_chave':'novo_valor'})

# # if d1.get('nova_chave') is not None:
# #     print(d1.get('nova_chave'))


# # print(d1)


# """
# Para excluir algo do dicionário:
# """

# # del d1['str']

# # print(d1)


# print('str' in d1)  # otp = True  """está checkando as chaves"""
# print('str' in d1.keys())  # otp = True  """está checkando as chaves"""
# print('valor' in d1.values())  # otp = True está acessando os valores

# # para saber a quantidade de pares que o dicionário têm:

# print(len(d1))  # otp = 3

# # pode iterar sobre o dicio:

# for k in d1:  # pega as chaves
#     print(k)  # otp = str \ 123 \ (1, 2, 3)

# for v in d1.values():  # pega os valores
#     print(v)  # otp = valor \ Outro valor \ Tupla

# for i in d1.items():  # acessa cada chave:valor em forma de tupla
#     print(i)  # otp = ('str', 'valor') \ (123, 'Outro valor') \ ((1, 2, 3), 'Tupla')
#     print(i[0], i[1])  # acessa chave e valor separadamente

# # para não usar indice:

# for k, v in d1.items():
#     print(k, v)


clientes = {
    'cliente1': {
        'nome': 'Sara',
        'sobrenome': 'Tavares'
    },
    'cliente2': {
        'nome': 'Jane',
        'sobrenome': 'Centeno'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'exibindo: {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

        # otp = 
# exibindo: cliente1                 # laço 1
#         nome = Sara                # laço 2
#         sobrenome = Tavares        # laço 2
# exibindo: cliente2
#         nome = Jane
#         sobrenome = Centeno


d1 = {1:'a', 2:'b', 3:'c'}
v = d1

v[1] = 'Luiz'

print(v)
print(d1)