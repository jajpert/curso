"""
21. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um 
conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, 
bem como a média das temperaturas.
"""


print("\nDepartamento Estadual de Meteorologia\n")
print("Para sair digite 0")
print("Digite as temperaturas a seguir:")
dados = []
maior = 0
menor = 9999999
soma = 0

while True:
    try:
        temp = float(input())
        dados.append(temp)

        if temp == 0:
            print(f"\nA maior temperatura é {maior}")
            print(f"A menor temperatura é {menor}")
            print(f"A média das temperaturas é {media:.2f}")
            break

        else:

            for d in dados:
                if d > maior:
                    maior = d
                
                if d < menor:
                    menor = d

                soma += d
            media = soma / len(dados)
    
    except ValueError:
        print("Valor inválido")
