"""
22. Os números primos possuem várias aplicações dentro da Computação, por exemplo na criptografia. Um 
número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número 
inteiro e determine se ele é ou não um número primo.
"""


num = int(input("\nDigite um número a seguir: ")) 

if num > 1:
    for n in range(2, num):
        if num % n == 0:
            print(f"Este número não é primo")
            break
    else:
        print("Este número é primo")

else:
    print("Este número não é primo")