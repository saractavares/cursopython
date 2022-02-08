"""
crie uma função que receba 2 numeros. o primeiro é um valor e o segundo
uma porcentagem (10% p.ex.). Retorne (return) o valor do primero
numero somado ao valor do aumento percentual do mesmo
"""


def aumento(num=int(input("numero 1: ")), perc=float(input("aumento percentual: "))):

    return num + (num * perc/100)


ap = aumento()
print(ap)
