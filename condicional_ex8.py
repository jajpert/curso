"""
8 - Faça um programa que pergunte o preço de três
produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato
"""

print("\nBem vindo ao programa melhor preço!\n")

print("Digite os 3 valores a seguir:")

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 < n2 and n1 < n3:
    print(f"O primeiro produto é de melhor preço: {n1}")

elif n2 < n1 and n2 < n3:
    print(f"O segundo produto é de melhor preço: {n2}")

elif n3 < n1 and n3 < n2:
    print(f"O terceiro produto é o de melhor preço: {n3}")
