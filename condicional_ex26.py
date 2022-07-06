"""
26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser 
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro 
do álcool é R$ 1,90.
"""

tipo = input("\nDigite A para álcool e G para gasolina: ")

tipo = tipo.lower()

if tipo == "a":
    
    litros = float(input("Digite quantos litros você quer: "))
    
    if litros <= 20:
        preco = litros * (1.9 - (0.03 * 1.9))

    elif litros >= 21:
        preco = litros * (1.9 - (0.05 * 1.9))

    elif litros < 0:
        print("Valor inválido")

    print(f"\nO valor a ser pago é R${preco:.2f}\n")

elif tipo == "g":
    
    litros = float(input("Digite quantos litros você quer: "))

    if litros <= 20:
        preco = litros * (2.5 - (0.04 * 2.5))

    elif litros >= 21:
        preco = litros * (2.5 - (0.06 * 2.5))

    elif litros < 0:
        print("Valor inválido")

    print(f"\nO valor a ser pago é R${preco:.2f}\n")

else:
    print("Valor inválido. Reinicie o programa.")

