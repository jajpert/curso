"""
6 - Faça uma função que informe a quantidade de dígitos de um determinado
número inteiro informado.
"""


def qtd_digitos(num):
    if  num.replace(".", ""):
        novo_num = num.replace(".", "")
        digitos = len(novo_num)
        print(f"Este número {num} tem {digitos} dígitos")

    else: 
        digitos = len(num)  
        print(f"Este número {num} tem {digitos} dígitos")


num = input("\nDigite um número a seguir: ")

qtd_digitos(num)