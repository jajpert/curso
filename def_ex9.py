"""
9 - Data com mês por extenso. Construa uma função que receba uma data no
formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso
de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja
inválida.
"""


def mesExtenso(data):
    if data[2] == 0:
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro"]
        mes_extenso = meses[data[3] - 1]
        return mes_extenso

    elif data[2] == 1:
        meses = ["outubro", "novembro", "dezembro"]
        mes_extenso = meses[data[3] - 1]
        return mes_extenso


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
    print("\nNULL\n")

elif int(data[2]) > 1 or  int(data[2]) < 0:
    print("\nNULL\n")

else:
    print(f"\n{data[0]}{data[1]} de {mesExtenso(data)} de {data[4]}{data[5]}{data[6]}{data[7]}")