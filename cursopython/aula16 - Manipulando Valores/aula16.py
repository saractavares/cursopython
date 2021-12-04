"""
:s - Texto (strings)
:d - Inteiros
:f - float
:.(número)f - Quantidade de casas decimais após a vírgula
:(caractere)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

nome = 'Sara tavares'
num = 22

print(nome)
print(type(f'{nome:*^20}'.title().casefold()))
