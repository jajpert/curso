"""
21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque 
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 
1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se 
preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""

valor = int(input("\nEntre com o valor a ser sacado: "))

cedulas = [100, 50, 20, 10, 5, 2, 1]

print(f"\nPara sacar a quantia de R${valor} serão necessárias:")
for cedula in cedulas:
    quantidade_cedulas = int(valor / cedula)

    print(f"{quantidade_cedulas} nota(s) de R$ {cedula},00\n")
    
    valor -= quantidade_cedulas * cedula
