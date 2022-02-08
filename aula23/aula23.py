"""
for/else
"""

var = ['Sara', 'Centeno', 'Tavares']

for valor in var:
    print(valor)
    if valor.startswith('S'):
        break
        print(valor)
else:
    print('Não existe uma palavra com a letra "S"')