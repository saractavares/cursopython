"""
Operador Ternário
"""

logged_user = False

if logged_user:
    msg = "User Logged"
else:
    msg = "Login enabled"

print(msg)

# Ternário:

msg = "User logged" if logged_user else 'Login enabled'

print(msg)

idade = input('Idade: ')
if not idade.isnumeric():
    print('só números')

else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Pode acessar' if e_maior else 'Não pode'

    print(msg)
