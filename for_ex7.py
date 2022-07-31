"""
7. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números 
pares e a quantidade de números ímpares.
"""

lista = []

for rep in range(10):
    n = int(input("Entre com um número: "))
    lista.append(n)

par = impar = 0

for item in lista:
    if item % 2:
        impar += 1
    
    else:
        par += 1

print(f"Há {par} número(s) par(es)")
print(f"Há {impar} número(s) ímpar(es)")