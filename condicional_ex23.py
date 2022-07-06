"""
23 - Faça um Programa que peça um número e
informe se o número é inteiro ou decimal. Dica:
utilize uma função de arredondamento.

"""

import math

n1 = input("\nDigite um número para saber se ele é decimal ou inteiro: ")

if float(n1) == math.floor(float(n1)):
    print("\nEste número é inteiro.\n")
else:
    print("\nEste número é decimal.")
