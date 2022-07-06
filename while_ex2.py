"""
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as 
informações.
"""

while True:
    try:
        nome = input("Digite seu nome a seguir: ")
        senha = input("Digite a senha: ")

        if nome == senha:
            raise NameError

        break
    except NameError:
        print("Você errou parabéns. Escreve certo agora.")
        continue