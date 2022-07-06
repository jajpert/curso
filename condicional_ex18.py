"""
18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""


print("\nBem vindo\n")

data = []
print("Digite uma data a seguir: ")

while True:
    data_em_string = input()
    for caract in data_em_string:
        if caract.isdigit():
            data.append(int(caract))

    if len(data) != 8:
        print("Entre uma data válida para ser verificada!\n")
        data.clear()
    else:
        break

if int(data[0]) > 3 or int(data[0]) < 1:
    print("\nData inválida!\n")

elif int(data[2]) > 1 or  int(data[2]) < 0:
    print("\nData inválida!\n")

else:
    print("\nA data é válida!\n")
