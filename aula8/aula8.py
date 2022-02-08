"""
resolução do desafio aula7
"""

nome = "Sara"
idade = 23
altura, peso = 1.61, 63
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso/(altura**2)

print('{0} tem {1} anos, {2} de altura e pesa {3}kg. \nO imc de {0} é {4:.2f}. \n{0} nasceu em {5}'.format(nome, idade, altura, peso, imc, nascimento))