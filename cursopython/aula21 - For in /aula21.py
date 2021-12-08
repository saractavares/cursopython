"""
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

texto = 'Python'

for letra in texto:
    print(letra)  # printa somente a letra naquele índice naquela volta do looping
print('\n------------||-------------')
################################

for n, letra in enumerate(texto):
    print(n, letra)  #função enumerate pega a volta que o looping está, printamos a volta com 'n'
print('\n------------||-------------')
################################

for numero in range(10):
    print(numero)
print('\n------------||-------------')

"""
Conceito de "Range"

sintaxe:
for <variavel qlqr> in range(<valor a ser analisado>) EXEMPLO:
    for i in range(5,18,3)
    onde:
    5 -> numero que começa
    18 -> numero até onde vai 
    3 -> intervalo (pula de 3 em 3 começando em 5)

"""
