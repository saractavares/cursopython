perguntas = {
    'pergunta1' : {
        'pergunta': 'Quanto é 1+1? ',
        'opções' : {'a':1, 'b':2, 'c':3},
        'correta': 'b',
    },
    'pergunta2' : {
        'pergunta': 'Quanto é 1-1? ',
        'opções' : {'a':0, 'b':2, 'c':3},
        'correta': 'a',
    },
    'pergunta3' : {
        'pergunta': 'Quanto é 1/1? ',
        'opções' : {'a':10, 'b':2, 'c':1},
        'correta': 'c',
    },
}

qnt_acertos = 0

for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')
    print('Opções:')
    for rk, rv in pv['opções'].items():
        print(f'[{rk}]: {rv}')
    resposta_user=input('Sua resposta: ')

    if resposta_user == pv['correta']:
        print('acertou')
        qnt_acertos += 1
    else:
        print('errou')

qnt_perguntas = len(perguntas)
porc_acertos = qnt_acertos/qnt_perguntas * 100

print(f'Você acertou {qnt_acertos} respostas.')
print(f'Seu percentual de acertos foi de: {porc_acertos}%.')