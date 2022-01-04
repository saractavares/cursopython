"""
Formas de construir dicionários:
"""
# d1 = {'chave1': 'valor da chave'}  # escrevendo cada chave e cada valor
# d1 = dict(chave1='valor1', chave2='valor2')  # com a função dict
# d1['nova_chave'] = 'nova_chave_valor'  # plotando valor no último index com colchetes

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3): 'Tupla'
}  # todos esses podem ser chaves em um dicionário

print(d1[(1, 2, 3)])  # output : Tupla
