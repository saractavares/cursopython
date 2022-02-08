"""
crie uma funcao1 que recebe uma fuincao2 como parametro e retorne o valor da funcao2 executada.
Faça a funcao1 executar duas funções que recebam um número diferente de argumentos.
"""
produtos = ''
total = 0


def comprar():
    items = input("Compras: ")
    global produtos
    produtos += items


def pagar():
    if produtos is None:
        print("Sem compras hoje")
    else:
        if len(produtos) > 4:
            global total
            total += 10.00
            print(type(produtos), total)
        elif len(produtos) <= 4:
            total += 5.00


def fazer_compras(*args):
    dinheiro = input("tem dinheiro?: Sim/Não = ")
    if dinheiro == 'Sim' or dinheiro == "sim" or dinheiro == 's' or dinheiro == 'S':
        return comprar(), pagar()
    print("então sem compras hoje!")


fazer_compras()

print(produtos, total)
