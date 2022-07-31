"""
26. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""


maior_cod = 0
menor_cod = 0
maior_indice = 0
menor_indice = 9999999999
total_carros = 0
cidade_2000 = 0
acid_2000 = 0

for cont in range(1, 6):
    cod = int(input("\nDigite o código da cidade: "))
    carros = int(input("Digite o número de veiculos de passeio: "))
    num_aci = int(input("Digite o número de acidentes com vítimas: "))

    indice = num_aci / carros
    total_carros += carros
    
    if indice > maior_indice:
        maior_indice = indice
        maior_cod = cod

    if indice < menor_indice:
        menor_indice = indice
        menor_cod = cod

    if carros < 2000:
        cidade_2000 += 1
        acid_2000 += 1

media_carro = total_carros / 5

print(f"\nO maior índice ({maior_indice:.5f}%) de acidentes de trânsito ocorreram na cidade de código {maior_cod}.")
print(f"O menor índice ({menor_indice:.5f}%) de acidentes de trânsito ocorreram na cidade de código {menor_cod}.")

print(f"A média de veiculos das 5 cidades juntas é {media_carro:.1f}")

if cidade_2000 > 0:
    media_2000 = acid_2000 / cidade_2000
    print(f"A média de acidentes nas cidades com menos de 2000 veículos de passeio é {media_2000:.2f}")