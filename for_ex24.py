"""
24. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""


g = int(input("Digite um número pra saber sua tabuada: "))
h = int(input("Digite de qual número ela deve começar: "))
j = int(input("Digite em qual deve parar: "))

print()

if h > j:
    h, j = j, h

for i in range(h, j + 1):
    print(f"{g} * {i} = {i * g}")

print()