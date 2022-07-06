"""
6 - Faça um Programa que leia três números e mostre o
maior deles.

"""

print("Digite 3 números a seguir:")

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print(f"Este é o maior número: {n1}")

elif n2 > n1 and n2 > n3:
    print(f"Este é o maior número: {n2}")

elif n3 > n1 and n3 > n2:
    print(f"Este é o maior número: {n3}")
