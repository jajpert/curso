"""
25 - Faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:

"Telefonou para a vítima?"

"Esteve no local do crime?"

"Mora perto da vítima?"

"Devia para a vítima?"

"Já trabalhou com a vítima?“

O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

print("\nResponda as perguntas com 0 para não e 1 para sim.")

while True:
    try:

        n1 = int(input("Telefonou para a vítima? "))
        if n1 < 0 or n1 > 1:
            raise ValueError
        
        n2 = int(input("Esteve no local do crime? "))
        if n1 < 0 or n1 > 1:
            raise ValueError

        n3 = int(input("Mora perto da vítima? "))
        if n1 < 0 or n1 > 1:
            raise ValueError

        n4 = int(input("Devia para a vítima? "))
        if n1 < 0 or n1 > 1:
            raise ValueError

        n5 = int(input("Já trabalhou com a vítima? "))
        if n1 < 0 or n1 > 1:
            raise ValueError

        soma = n1 + n2 + n3+ n4 + n5

        if soma == 2:
            print("\nVocê está classificado como suspeito\n")
        
        elif soma == 3 or soma == 4:
            print("\nVocê está classificado como cúmplice\n")

        elif soma == 5:
            print("\nVocê é o assassino!\n")

        else:
            print("\nVocê é inocente.\n")

        break

    except ValueError:
        print("Valor inválido. Recomece o jogo e digite apenas 0 ou 1 para as respostas!")
