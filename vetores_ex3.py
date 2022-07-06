"""
Faça um Programa que receba um vetor de 5 frutas mostre-os.

Depois, substitua o segundo elemento do vetor por Laranja.

"""

aq = []

cont = int(input("\nDigite quantas frutas serão inseridos: "))

print("\nDigite as frutas a seguir: ")

n = 1 

while n <= cont:
    fruta = input()

    aq.append(fruta)

    n += 1

del aq[1]
aq.insert(1, "laranja")

print(aq)