"""
25. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e 
o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o 
número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""


dicio = {}

for i in range(1, 11):
    num_aluno = int(input("\nDigite o código do aluno: "))
    alt = int(input("Digite a altura do aluno: "))

    dicio[num_aluno] = alt


def achar_chave(arg):
    for key, value in dicio.items():
        if arg == value:
            return key

maior = max(dicio.values())
menor = min(dicio.values())

maior_cod = achar_chave(maior)
menor_cod = achar_chave(menor)

print(f"\nO código do maior aluno é {maior_cod} e sua altura é {maior} cm.")
print(f"O código do menor aluno é {menor_cod} e sua altura é {menor} cm.")
