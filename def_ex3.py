"""
3- Faça um programa com uma função chamada somaImposto. A função possui dois 
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função
"altera" o valor de custo para incluir o imposto sobre vendas.
"""


def somaImposto(taxaImposto, custo):
    preco = custo + (custo * (taxaImposto/100))
    print(f"Com o imposto incluido fica R${preco:.2f}")


taxaImposto = float(input("Digite a taxa do imposto: "))
custo = float(input("Digite o custo: "))

somaImposto(taxaImposto, custo)