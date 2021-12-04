"""
Documentação
"""

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

#print(num1 + num2)

# if num1.isnumeric() and num2.isnumeric():
try:
    num1, num2 = float(num1), float(num2)
    print(num1 + num2)
# else:
except:
    print("Digite números!")

