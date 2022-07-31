"""
17. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de
CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e
o valor para cada um.
"""


num = int(input("Digite quantos CD's existem em sua coleção: "))

soma = 0

for qtd in range(num):
    preco = float(input("Digite o preço do CD: "))

    while preco < 0:
        print("Valor inválido")
        preco = float(input("Digite novamente o preço do CD: "))

    soma += preco

media = soma / num

print(f"\nExistem na coleção {num} CD(s).")
print(f"O valor médio gasto em cada um dele foi de R${media:.2f}.")
