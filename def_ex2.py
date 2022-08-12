"""
2- Faça um programa, com uma função que necessite de um argumento. A função
retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se 
seu argumento for 0 ou negativo
"""


def aqui(num):
    if num > 0:
        print("P")
    else:
        print("N")

aqui(10)
aqui(-10)