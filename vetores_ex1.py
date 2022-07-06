"""
Faça um Programa que receba um vetor de 5 números inteiros e mostre-os.
Mostre o maior deles;
Mostre o menor deles;
Mostre a quantidade de números;
Some os números;
"""

aqui = []

cont = int(input("\nDigite quantos vetores serão inseridos: "))

print("\nDigite os números a seguir:")

n = 1

while n <= cont:
    num = int(input())
    aqui.append(num)
    
    n += 1

print(f"\nExistem {len(aqui)} item(ns) na lista")
print(f"\nO maior valor da lista é {max(aqui)}")
print(f"\nO menor valor da lista é {min(aqui)}")
print(f"\nA soma dos valores da lista é {sum(aqui)}\n")