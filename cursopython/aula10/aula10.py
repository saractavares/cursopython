"""
condições = IF, ELIF e ELSE
"""
nome = input("nome: ")
idade = input("idade: ")
idade = float(idade)
menor = 20
maior = 30

if menor <= idade <= maior:
    print(f'{nome} tem {idade} e pode pegar empréstimo')
else:
    print(f'{nome} não pode pegar empréstimo')
