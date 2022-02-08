"""
len - Quantidade de caracteres
"""

string1 = input("digite alog: ")
string2 = input("digite outra coisa: ")

tam_aceitavel = 8

"""
tem 2 métodos:
len(objeto)
objeto.__len__()
"""
if string1.__len__() >= tam_aceitavel:
# if len(string1) >= tam_aceitavel:
    print('Aceitável')
else:
    print(f'string deve ter {tam_aceitavel} caractéres ou mais')



# print(len(string1))
# print(string2.__len__())


