"""
while em Python
Utilizado para realizar operações "enquanto" uma condição for verdadeira


"""

# while True:
#     nome = input('Qual seu nome? \n')
#     print(f'Olá {nome}')
#     break

# x = 97
# while x <= 100:
#     print(x)
#     x = x+2

# x = 0  # coluna
# while x < 10:
#     y = 0  # linha
#     while y < 5:
#         print(f'X vale {x} e Y vale {y}')
#         y += 1
#
#     x += 1
#
# print('Acabou')
from itertools import repeat

print('---------------------\n* Calculadora Iniciada *\n---------------------')

while True:
    print()
    num1 = input('Digite um número: ')
    ope = input('Digite uma operação: ')
    num2 = input('Digite outro número: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Use somente números!')
        continue
    num1 = int(num1)
    num2 = int(num2)

    # + - / *
    if ope == '+':
        print(num1 + num2)
    elif ope == '-':
        print(num1 - num2)
    elif ope == '/':
        print(num1 / num2)
    elif ope == '*':
        print(num1 * num2)
    else:
        print('Operador inválido')
        print()

    continuar = input('Deseja continuar? s/n : ')
    for i in continuar:
        if continuar == 's':
            print()
        elif continuar == 'n':
            print('---------------------\n* Calculadora finalizada *\n---------------------')
            break
        else:
            print('Opção inválida')
            continuar = input('Deseja continuar? s/n : ')
