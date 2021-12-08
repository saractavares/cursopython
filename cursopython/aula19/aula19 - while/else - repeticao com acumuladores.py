"""
While/Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 100:
    print(contador, acumulador)

    if contador > 5:
        break
        
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else 2')
print('Cheguei no else 1')