"""
CPF = 168.995.350-09
___________________________________
receber o CPF
retirar os pontos e traços e guardar em uma nova var
percorrer os primeiros 9 digitos
* 10 até *2 (range(10, 1, -1)
var_soma = somando todos os resultados
var confirmacao = 11 - (var_soma % len(CPF))
if confirmacao == 11 and confirmacao > 9
var digito1 = 0

percorrer os primeiros 10 digitos
* 11 até *2 (range(11, 1, -1)
var_soma = somando todos os resultados
var confirmacao = 11 - (var_soma % len(CPF))
if confirmacao == 11 and confirmacao > 9
var digito1 = 0
"""
import re

CPF = input("Qual o CPF: ")
CPF = (re.sub("\!|\'|\?|\.|\-", "", CPF))
novo_cpf = CPF[:-2]
reverso = 10
total = 0

for i in range(19):
    if i > 8:
        i -= 9

    total += int(novo_cpf[i]) * reverso

    print(novo_cpf[i], reverso)

    reverso -= 1

    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0

            novo_cpf += str(d)


print(novo_cpf)

if CPF == novo_cpf:
    print('válido')
else:
    print('inválido')

#  451.078.278-02