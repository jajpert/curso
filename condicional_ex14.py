"""
14 - Faça um programa que leia as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se
o conceito for D ou E.
"""

n1 = float(input("Digite a sua primeira nota parcial: "))
n2 = float(input("Digite a sua segunda nota parcial: "))

media = (n1 + n2) / 2

if media >= 9 and media <= 10:
    media_apro = "A"
    aprov = "APROVADO"
    
elif media <= 8.9 and media >= 7.5:
    media_apro = "B"
    aprov = "APROVADO"

elif media <= 7.4 and media >= 6:
    media_apro = "C"
    aprov = "APROVADO"

elif media <= 5.9 and media >= 4:
    media_apro = "D"
    aprov = "REPROVADO"

elif media <= 3.9 and media >= 0:
    media_apro = "E"
    aprov = "REPROVADO"

print(f"Sua média de aproveitamento é {media_apro} e você está {aprov}")
