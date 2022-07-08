"""
9 – Em uma eleição presidencial existem quatro candidatos.

Os votos são informados através de códigos. Os dados utilizados para a contagem
dos votos obedecem à seguinte codificação:

1,2,3,4 = voto para os respectivos candidatos;

5 = voto nulo;

6 = voto em branco;

Elabore um programa que leia o código votado por vários eleitores. Como
finalizador da entrada de dados, considere o código zero.

Ao final, calcule e escreva:

total de votos para cada candidato;

- total de votos nulos;

- total de votos em branco;
"""

print("\nEleição presidencial")
print("Siga as instruções a seguir:")
print("Digite 1,2,3,4 para os respectivos candidatos")
print("Digite 5 para voto nulo")
print("Digite 6 para voto em branco")

escolha = int(input("\nDigite seu voto a seguir: "))
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto6 = 0

while True:
        
    if escolha == 1:
        voto1 += 1

    elif escolha == 2:
        voto2 += 1

    elif escolha == 3:
        voto3 += 1

    elif escolha == 4:
        voto4 += 1

    elif escolha == 5:
        voto5 += 1

    elif escolha == 6:
        voto6 += 1

    elif escolha < 0 or escolha > 6:
        print("Valor inválido")

    elif escolha == 0:
        break

    escolha = int(input("\nDigite seu voto a seguir: "))
        

print(f"\nO candidato 1 teve {voto1} voto(s).")
print(f"O candidato 2 teve {voto2} voto(s).")
print(f"O candidato 3 teve {voto3} voto(s).")
print(f"O candidato 4 teve {voto4} voto(s).")
print(f"Tiveram {voto5} voto(s) nulo(s).")
print(f"Tiveram {voto6} voto(s) em branco.\n")

