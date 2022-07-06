"""
17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se 
este ano é ou não bissexto.
"""


ano = int(input("\nDigite um ano para saber se ele é bissexto ou não: "))

if ano % 4 == 0:
    print("\nEste ano é bissexto.")

else: 
    print("\nEste ano não é bissexto.")
