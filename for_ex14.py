"""
14. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido
pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes
(divisões) executados.
"""


n = int(input("\nDigite um número a seguir: "))

divisao = 1
qtd_primo = 1
primos = [2,]

for num in range(3, n + 1):
    for i in primos:
        if num % i == 0: 
            break
        divisao += 1
    else:
        primos.append(num)
        qtd_primo += 1

print(f"\nForam encontrados {qtd_primo} números primos, {primos}.")
print(f"Foram necessárias {divisao} comparações.")