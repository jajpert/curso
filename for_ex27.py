"""
27- Faça um programa que peça um número inteiro positivo e em seguida mostre este número invertido.
"""

num = input("Digite um número a seguir: ")

lista = [n for n in reversed(num)]
print(f"\nO reverso do número {num} é {''.join(lista)}\n")
