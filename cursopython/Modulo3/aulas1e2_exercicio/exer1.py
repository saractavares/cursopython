"""
crie uma função que exibe uma saudação com os parâmetros saudacao e nome
"""


def ola(saudacao='Oi', nome=input('nome: ')):
    comprimento = f'{saudacao} {nome}'
    print(comprimento)


ola()
