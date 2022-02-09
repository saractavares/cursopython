"""
Set significa conjunto em inglês. A sintaxe é set = {}, parecido com dicionário,
porém, não é chave e valor: exemplo: set1 = {1,2,3,4} - isso é um set.
Além disso, um set só permite valores unicos. Ou seja, se eu quiserr unir 
2 sets, todos os valores duplicados serão anulados.
Também, sets não respeitam nenhuma ordem, seu output é sempre aleatório.

Manipulação de sets:
-> " | "(pipe) = une sets
-> " - " = traz os valores unicos diferentes do set da esquerda: primeiro set escrito:
ex.:
set1 = {1,2,3,4}
set2 = {1,2,3}

set3 = set1 - set2

print(set3)
----------
otp:
{4}  # é o valor único que só existe no set escrito primeiro na variável set3

" ^ " = traz todos os valores diferentes entre sets:
ex.:
set1 = {1,2,3,4}
set2 = {1,2,3,5}

set3 = set1 ^ set2

print(set3)
----------
otp:
{4,5}
"""

