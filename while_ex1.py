"""
1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso 
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

while True:
    try:
        nota = float(input("Digite sua nota aqui: "))

        if nota < 0 or nota > 10:
            raise ValueError
        
        else:
            print("Acertou amém")
            break

    except ValueError:
        print("Coloca o número certo ai vai")
        continue