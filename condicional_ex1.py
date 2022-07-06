"""
1 - Faça um Programa que peça dois números e
imprima o maior deles.
"""

num1, num2 = input("Digite 2 números a seguir: ").split()
num1 = int(num1)
num2 = int(num2)

maior = max(num1, num2)

print(maior, "é o maior.")
