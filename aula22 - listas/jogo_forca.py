palavra = 'RIVOTRIL'
digitadas = []
# numero de chances
chances = 3

while True:

    if chances <= 0:
        print('GAME OVER')
        break
    
    # recebendo letra do usuário
    letra = input('Digite uma letra: ')
    letra = letra.upper()
    
    if len(letra) > 1:
        print('Inválido! Digite apenas 1 letra')
        continue

    digitadas.append(letra)

    if letra in palavra:
        print('Acertou')
    else:
        print('Errou')
        digitadas.pop()

    palavra_temp = ''
    for letra_temp in palavra:
        if letra_temp in digitadas:
            palavra_temp += letra_temp
        else:
            palavra_temp += '*'
    
    if palavra_temp == palavra:
        print(f'UHUUULLL você ganhou! A palavra era {palavra}')
        break
    else:
        print(f'A palavra está assim : {palavra_temp}')

    if letra not in palavra:
        chances -= 1

    print(f'Você ainda tem {chances} tentativas')
    print()