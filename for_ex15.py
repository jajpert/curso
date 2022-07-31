"""
15. Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se
a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é
jovem, adulta ou idosa, conforme a média calculada.
"""


num = int(input("Digite quantas idades serão inseridas: "))

soma = 0

for people in range(num):
    idade = int(input("\nDigite sua idade a seguir: "))

    soma += idade

media = soma / num

print()

if media >= 0 and media <= 25:
    print(f"A média da turma varia entre 0 e 25, logo ela é jovem.")

elif media >= 26 and media <= 60:
    print(f"A média da turma varia entre 26 e 60, logo ela é adulta.")

elif media > 60:
    print(f"A média da turma varia entre 0 e 25, logo ela é idosa.")