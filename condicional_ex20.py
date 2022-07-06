"""
20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular 
a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

print("Digite suas notas a seguir: ")

n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3) / 3

if media == 10:
    print(f"Aprovado com distinção!!")

elif media >= 7:
    print(f"Aprovado, sua média foi {media:.2f}")

elif media <= 7:
    print(f"Reprovado, sua média foi {media:.2f}")
