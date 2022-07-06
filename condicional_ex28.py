"""
28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: (imagem)

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da 
promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for feita 
no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva 
um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
valor do desconto e valor a pagar.

"""

print("\nBem vindo a promoção do Hipermercado Tabajara!\n")

carne = int(input("Digite a carne que deseja comprar (1 - file duplo, 2 - alcatra, 3 - picanha): "))

peso = float(input("Digite quantos quilos de carne você deseja: "))

pagamento = int(input("Digite o tipo de pagamento (1 - dinheiro ou outros, 2 - cartão tabajara): "))

if carne == 1:
    if peso <= 5:
        preco = peso * 4.9
    else:
        preco = peso * 5.8

elif carne == 2:
    if peso <= 5:
        preco = peso * 5.9
    else: 
        preco = peso * 6.8

elif carne == 3:
    if peso <= 5:
        preco = peso * 6.9
    else:
        preco = peso * 7.8

if pagamento == 2:
    desconto = preco * 0.05
    pagamento = "cartão tabajara"
    valor_total = preco - desconto

elif pagamento == 1:
    desconto = 0
    pagamento = "dinheiro ou outros"
    valor_total = preco

print("\nCupom Fiscal")
print("Tipo de carne:", carne)
print(f"Quantidade: {peso:.2f} kg")
print(f"Preço total: R${preco:.2f}")
print("Tipo de pagamento:", pagamento)
print(f"Valor do desconto: R${desconto:.2f}")
print(f"Valor a pagar: R${valor_total:.2f}")
