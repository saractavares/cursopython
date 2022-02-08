"""
crie uma funcao1 que recebe uma fuincao2 como parametro e retorne o valor da funcao2 executada
"""


def func1():
    nome = input('Qual seu nome?: ')
    return nome


def func2():
    return func1()


print(func2())
