"""
16. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a
quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais
de 40 alunos.
"""


qtd_turmas = int(input("Digite a quantidade de turmas: "))

soma = 0

for i in range(qtd_turmas):
    
    qtd_alunos = int(input("Digite a quantidade de alunos na sala: "))
    
    while qtd_alunos > 40 or qtd_alunos < 1:
        print("Valor inválido")
        qtd_alunos = int(input("Digite a quantidade de alunos na sala: "))
    
    else:
        soma += qtd_alunos    

media = soma // qtd_turmas

print(f"O número médio de alunos por turma é {media}")