"""
8. A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa 
capaz de gerar a série até o enésimo termo.
"""

n = int(input("Digite quantos termos serão: "))

ultimo = 1
penultimo = 1

if n == 1:
    print(ultimo)

elif n == 2:
    print(ultimo)
    print(penultimo)

else:
    print(ultimo)
    print(penultimo)
    for i in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo)
        