"""
Manipulando strings
*String indices
*fatiamento de strings [inicio:fim:passo]
*funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

doc.:
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html


"""
# positivos
#  [012345678]
texto = 'Python s2'

print(texto[::-2])  # 2 otP

print(f'{texto[::-2].__len__()} é o tamanho dessa string')

n = 58 / 8

print(n.__abs__())


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
