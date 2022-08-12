"""
8 - Jogo de Craps. Faça um programa de implemente um jogo de Craps. O
jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira
jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12
na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira
jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é
continuar jogando os dados até tirar este número novamente. Você perde, no
entanto, se tirar um 7 antes de tirar este Ponto novamente.
"""


from random import randint

def joga_dados():
    dados = randint(2, 12)
    return dados

dados = joga_dados()
print("A soma dos dados deu", dados)

if dados == 7 or dados == 11:
    print("\nVocê ganhou! Parabéns por ser um natural!!")

elif dados == 2 or dados == 3 or dados == 12:
    print("\nCraps. Você perdeu!")

else:
    print("\nSeu ponto é", dados)
    meta = dados

    escolha = input("\nDigite 0 para parar o jogo e qualquer outra tecla para continuar jogando: ")

    if escolha == 0:
        print("Você terminou o jogo")

    else: 
        while True:
            dados = joga_dados()
            print("A soma dos dados deu", dados)
            
            if dados == meta:
                print("\nVocê ganhou!!")
                break

            elif dados == 7:
                print("\nVocê perdeu!")
                break
            
            else:
                print("Continue tentando")

            escolha = input("\nDigite um número para jogar os dados: ")

            if escolha == "0":
                print("Você terminou o jogo")
                break
