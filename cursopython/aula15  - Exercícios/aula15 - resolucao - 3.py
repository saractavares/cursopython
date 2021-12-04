"""
Exercício 03: Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver quatro letras ou menos, escreva "seu nome é curto".
Se tiver entre cinco e seis letras, escreva "seu nome é normal".
Se tiver mais de seis letras, escreva "seu nome é muito grande".
"""

nome = input('Qual seu nome?: ')

if not nome.isalpha() or nome.isspace():
    print('Inválido! Digite um nome somente com letras!')
elif 1 < nome.__len__() <= 4:
    print("Seu nome é curto!")
elif 4 < nome.__len__() < 7:
    print('Seu nome é normal')
elif 6 < nome.__len__():
    print('Seu nome é grande')
elif nome.__len__() <= 1:
    print('entrada de dado inválida, digite um nome com pelo menos 2 caracteres')
else:
    print('Retire caracteres especiais, números ou espaços em branco.')
