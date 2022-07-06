"""
27- Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo 
cliente.

Uma fruteira está vendendo frutas com a seguinte tabela (imagem)

"""

fruta = int(input("Digite 1 se você deseja comprar morango ou 2 para maçã: "))

if fruta == 1:
    quilo = float(input("Digite quantos quilos de morango você quer: "))

    if quilo <= 5:
        preco = quilo * 2.5
    else:
        preco = quilo * 2.2

elif fruta == 2:
    quilo = float(input("Digite quantos quilos de maçã você quer: "))

    if quilo <= 5:
        preco = quilo * 1.8
    else:
        preco = quilo * 1.5

else:
    print("\nReinicie o programa e digite um valor válido!\n")
    

if fruta == 1 or fruta == 2 and quilo >= 8:
    preco -= (preco * 0.1)

elif fruta == 1 or fruta == 2 and preco >= 25:
    preco -= (preco * 0.1)

print(f"A conta ficou no valor de R${preco:.2f}")