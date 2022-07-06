"""
13 - Faça um Programa que leia um número e
exiba o dia correspondente da semana. (1-
Domingo, 2- Segunda, etc.), se digitar outro valor
deve aparecer valor inválido.
"""

dia = int(input("Digite um número para saber o dia da semana correspondente: "))

if dia == 1:
    print("\nDomingo")

elif dia == 2:
    print("\n Segunda feira")

elif dia == 3: 
    print("\n Terça feira")

elif dia == 4:
    print("\n Quarta feira")

elif dia == 5:
    print("\n Quinta feira")

elif dia == 6:
    print("\n Sexta feira")

elif dia == 7 :
    print("\n Sábado")

else:
    print("Número inválido")
