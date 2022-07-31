"""
3. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
intervalo compreendido por eles.
"""

n = int(input("\nDigite o primeiro número: "))
j = int(input("Digite o segundo número: "))
print()

if j < n:
    j, n = n, j
    
for i in range(n + 1,j):
    print(i)
