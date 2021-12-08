"""
iterando strings com laço while


"""
#        indices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de Roma   '
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usr = input('Qual letra maiuscula?: ')

while contador < tamanho_frase:
    letra = frase['contador']
    if letra == input_do_usr:
        nova_string += input_do_usr.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
