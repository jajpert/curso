"""
5 - Altere o programa anterior permitindo ao usuário informar as
populações e as taxas de crescimento iniciais. Valide a entrada e
permita repetir a operação. 
"""

a = int(input("Digite a primeira população: "))
while a < 0:
    a = int(input("Digite um valor válido: "))

cres_a = float(input("Digite a primeira taxa de crescimento: "))
while cres_a < 0:
    cres_a = int(input("Digite um valor válido: "))
cres_a /= 100

b = int(input("Digite a segunda população: "))
while b < 0:
    b = int(input("Digite um valor válido: "))

cres_b = float(input("Digite a segunda taxa de crescimento: "))
while cres_b < 0:
    cres_b = int(input("Digite um valor válido: "))
cres_b /= 100

ano = 0

while a <= b:
    a += a * cres_a
    b += b * cres_b

    ano += 1

print("A população A ultrapassará ou igualará sua população com a B em", ano)