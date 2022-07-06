"""
9 - Faça um Programa que leia três números e mostre-
os em ordem decrescente.

"""

lista = []
x = 0

print("\nDigite os números a seguir: ")

while x != 3:
    number = float(input())
    lista.append(number)
    x += 1

lista.sort(reverse = True )

print(lista)
