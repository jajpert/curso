"""
12. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
(Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior 
valor e a soma dos valores.)
"""

lista = []
escolha = 0
maior_num = 0
menor_num = 1001
soma = 0

while True:
    escolha = int(input("Digite os números a seguir ou -1 para obter os resultados: "))
    
    if escolha == -1:
        break
    
    elif escolha < 0 or escolha > 1000:
        print("Valor inválido")
    
    else:
        lista.append(escolha)


for num in lista:
    if num > maior_num:
        maior_num = num

    if num < menor_num:
        menor_num = num

    soma += num

print("O maior número é", maior_num)
print("O menor número é", menor_num)
print("A soma de todos os números é", soma)