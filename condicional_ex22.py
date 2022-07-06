"""
22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo (resto da divisão).

"""

print("Digite um número para saber se ele é par ou ímpar:")
num = int(input())

if num % 2 == 0:
    print(num, "é par.")
else:
    print(num, "é impar.")
