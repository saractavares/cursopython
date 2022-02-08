"""
Funções - def em Python pt.1
"""


def funcao(msg=input("Say hi in your lang: "), lang=input("But wait! What's your lang?: ")):
    hi = f' "{msg}" means Hi in {lang}'
    # return f'{msg} {lang}'
    print(hi)


funcao()


