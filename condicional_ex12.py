"""
12 - Faça um programa para o cálculo de uma folha de
pagamento, sabendo que os descontos são do Imposto de
Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que
deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o
valor da sua hora e a quantidade de horas trabalhadas no
mês.Desconto do IR:
• Salário Bruto até 900 (inclusive) - isento
• Salário Bruto até 1500 (inclusive) - desconto de 5%
• Salário Bruto até 2500 (inclusive) - desconto de 10%
• Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora
é 220.
"""

print("\nCálculo da folha de pagamento")

valor_hora = float(input("Digite o valor da hora: "))
qnt_hora = float(input("Digite a quantidade de horas trabalhadas no mês: "))

sal_bruto = valor_hora * qnt_hora

if sal_bruto <= 900:
    ir = "ISENTO"
    fgts = sal_bruto * 0.11
    desc = fgts

elif sal_bruto >= 901 and sal_bruto <= 1500:
    ir = "5%"
    IR = sal_bruto * 0.05

elif sal_bruto >= 1501 and sal_bruto <= 2500:
    ir = "10%"
    IR = sal_bruto * 0.10

elif sal_bruto >= 2501:
    ir = "20%"
    IR = sal_bruto * 0.20

fgts = sal_bruto * 0.11
sal_liq = sal_bruto - desc

print(f"\nSalário Bruto : ({valor_hora} * {qnt_hora})                   : R$ {sal_bruto:7.2f}")
print(f"(-) IR ({ir})                                     : R$ {IR:7.2f}")
print(f"FGTS  (11%)                                     : R$ {fgts:7.2f}")
print(f"Total de descontos                              : R$ {IR:7.2f}")
print(f"Salário líquido                                 : R$ {sal_liq:7.2f}")
