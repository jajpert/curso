"""
7 - Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
""" 


def reverso_num(num):
    lista = [n for n in reversed(num)]
    print(f"\nO reverso do número {num} é {''.join(lista)}\n")


num = input("Digite um número a seguir: ")
reverso_num(num)