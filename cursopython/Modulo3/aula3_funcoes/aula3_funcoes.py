"""
Funções (def) - *arhs **kwargs - parte 3
"""


def func(*args, **kwargs):
    print(args)
    # print(kwargs['nome'], kwargs['sobrenome'])

    data = kwargs.get('data')
    if data is not None:
        print(data)
    else:
        print('não tem data')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
# n1, n2, *n = lista
func(*lista, *lista2, nome='Sara', sobrenome='Tavares', data='28/12/2021')

# var = func()
