"""
Funções (def) - return - parte 2
"""


def f(var):
    print(var)


def g():
    return f


var = g()

var("var pode fazer algo pois agora é uma função")


# retornar mais de um elemento faz virar tupla
def h():
    return ("coisa 1", "coisa 2")

out_var = h()
print(type(out_var))
