"""
desafio do imc
"""

nome = 'Sara Tavares'
idade = 23
altura = 1.61
e_maior = idade > 18
peso = 63
imc = peso/(altura*altura)
# print(nome, '\n', idade,'\n', altura, '\n', e_maior)

print(nome, ' tem ', idade, ' anos e seu imc é: ', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
