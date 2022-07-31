"""
20. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""


n = int(input("Fatorial de: "))

fatorial = 1
fator = []

for i in range(n, 0, -1):
    fatorial *= i
    fator.append(i)
    fator.append(".")

fator.pop()
print(f"{n}! =", *fator, "=", fatorial)