"""
Escopo de variáveis
"""

variavel = 'valor'  # está em escopo global


def func():
    print(variavel)  # está acessível por ser global


func()


def func2():
    # print(variavel2)  # não acessa variável local de outra função
    # print(variavel)
    global variavel
    variavel = 'outro valor'  # não é global, nada mais acessa a não ser a própria função
    print(variavel)  # aqui acessa localmente no escopo


func2()
print(variavel)  # mudou globalmente pois na func2 declarei global
