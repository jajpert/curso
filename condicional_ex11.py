"""
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

"""

print("\nBem vindo as Organizações Tabajara")

salario = float(input("\nDigite a seguir o valor atual do seu salário: "))

if salario <= 280:
    aumento = salario * 0.2
    salario_novo = salario + aumento
    percentual = "20%"

elif salario >= 281 and salario <= 700:
    aumento = salario * 0.15
    salario_novo = salario + aumento
    percentual = "15%"

elif salario >= 701 and salario <= 1500:
    aumento = salario * 0.1
    salario_novo = salario + aumento
    percentual = "10%"

elif salario >= 1501:
    aumento = salario * 0.05
    salario_novo = salario + aumento
    percentual = "5%"

print(f"\nSeu salário antes do reajuste era R${salario}")
print(f"Foi realizado um aumento percentual de {percentual}")
print(f"Logo o aumento foi de R${aumento:.2f}")
print(f"Seu salário após o aumento é R${salario_novo:.2f}\n")
