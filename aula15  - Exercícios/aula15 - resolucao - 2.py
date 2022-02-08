"""
Exercício 02: Fazer um programa que pergunte somente a hora do dia ao usuário.
Baseando-se no horário informado, exibe a saudação apropriada.
exemplo: de 0 às 11 "Bom dia!"; 12 às 17 "Boa tarde!" de 18 às 23 "Boa noite!".
Também tem o problema de a pessoa digitar alguma coisa que não seja um número de 0 a 23.
"""
# from datetime import time
import time

hora = input('No formato 01 - 24, que horas são?:\n')

if hora.isnumeric():
    if len(hora) == 2:
        if '06' <= hora <= '12':
            print('Bom dia!')
        elif '12' < hora <= '18':
            print('Boa Tarde!')
        elif '18' < hora <= '24':
            print('Boa noite!')
        elif hora > '24':
            print('Hora inválida, digite horas até 24!')
        else:
            print('É madrugada, vá dormir!')
    else:
        print('Quantidade de números inválida! Digite 2 números!')
else:
    print('Digito inválido, digite números inteiros!')
