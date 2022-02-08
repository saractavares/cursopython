"""
Exercício 01: Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este número par ou ímpar. Caso o usuário não digite o número inteiro, informe que o termo digitado
não é um número inteiro.
"""

num = input("Digite um número inteiro: ")
if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print("É par")
    else:
        print('É impar!')
else:
    print('Isso não é um número inteiro!')

