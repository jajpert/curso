"""
1- Faça um programa, com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos
"""


def total(*num):
    lista = [n for n in num]
    print(sum(lista))

total(22, 4, 5, )