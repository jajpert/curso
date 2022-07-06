"""
4 - Supondo que a população de um país A seja da ordem de
80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de
crescimento.
"""

a = 80000
cres_a = 0.03
b = 200000
cres_b = 0.015

ano = 0

while a <= b:
    a += a * cres_a
    b += b * cres_b

    ano += 1

print("A população A ultrapassará ou igualará sua população com a B em", ano)
