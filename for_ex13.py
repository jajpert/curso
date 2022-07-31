"""
13. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias 
vezes e limitando o fatorial a números inteiros positivos e menores que 16.
(Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.)
"""

print("Para sair digite -1")

while True:

    n = int(input("\nDigite um número a seguir: "))

    if n == -1:
        print("Você saiu")
        break

    elif n < 0 or n > 16:
        print("Valor inválido")

    else:
        fatorial = 1

        for i in range(n, 1, -1):
                fatorial *= i

        print("O resultado é", fatorial)