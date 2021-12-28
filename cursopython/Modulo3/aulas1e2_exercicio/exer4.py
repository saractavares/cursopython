"""
Fizz Buzz - Se o parametro da função for divisivel por 3, retorna Fizz
se for divisivel por 5, retorna buzz
se por 3 e por 5, fizz buzz
"""


def fizzbuzz():
    while True:

        numero = int(input('Numero: '))

        if numero == 0:
            print(f'{numero} não é divisível por nada')
            break

        if numero % 3 == 0 and numero % 5 == 0:
            return "Fizz Buzz"

        if numero % 3 == 0:
            return "Fizz"

        if numero % 5 == 0:
            return "Buzz"

        return numero

    resultado = fizzbuzz()
    print(resultado)


fizzbuzz()
