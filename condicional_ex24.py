"""
24 - Faça um Programa que leia 2 números e em
seguida pergunte ao usuário qual operação ele
deseja realizar. O resultado da operação deve ser
acompanhado de uma frase que diga se o
número é:

par ou ímpar;

positivo ou negativo;

inteiro ou decimal.
"""

print("\nCALCULADORA")

while True: 
    try:
        operacao = input("\nDigite qual operação deseja fazer (1 - adição, 2 - subtração, 3 - multiplicação, 4 - divisão): ")

        operacao = int(operacao)
            
        if operacao > 4 or operacao < 1:
            print("Reinicie o programa e digite um valor disponível")

        n1 = float(input("\nDigite o primeiro número a seguir: "))
        n2 = float(input("Digite o segundo número a seguir: "))

        if operacao == 1:
            result = n1 + n2

        elif operacao == 2:
            result = n1 - n2

        elif operacao == 3:
            result = n1 * n2

        else: 
            result = n1 / n2


        if result % 2 == 0:
            p_ou_i = "par"
        
        else:
            p_ou_i = "ímpar"


        if result > 0:
            p_ou_n = "positivo"
        
        else:
            p_ou_n = "negativo"


        import math

        if float(result) == math.floor(float(result)):
            i_ou_d = "inteiro"
            result = int(result)
        
        else:
            i_ou_d = "decimal"

        print(f"\nO resultado é {result}, este número é {p_ou_i}, {p_ou_n} e {i_ou_d}.\n")
        
        break
    except ValueError:
        print("\nValor inválido, digite números!")