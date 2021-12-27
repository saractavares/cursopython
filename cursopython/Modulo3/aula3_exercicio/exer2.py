"""
crie uma função que recebe 3 números como parametros e exiba a soma entre eles
"""


def soma(num1=int(input(f'Numero 1: ')), num2=int(input(f'Numero 2: ')), num3=int(input(f'Numero 3: '))):
    operacao = num1 + num2 + num3

    print(operacao)

    return soma


soma()
