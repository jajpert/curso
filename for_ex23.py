"""
23. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos 
existentes entre 1 e um número inteiro informado pelo usuário.
"""


n = int(input("\nDigite um número a seguir: "))

primos = [2,]

for num in range(3, n + 1):
    for i in primos:
        if num % i == 0: 
            break

    else:
        primos.append(num)


if n == 1:
    print("Não há números primos entre 1 e 1.")

elif n < 1:
    print("Valor inválido")

else:
    print(f"\nOs números primos existentes entre 1 e {n} são: {primos}")
