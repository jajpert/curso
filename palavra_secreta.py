secreto = "Julia"
digitadas = []
chances = 7

while True:
    if chances == 0:
        print("Você perdeu.")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Isso não vale... digite apenas uma letra")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f"Ebaaa, a letra {letra} existe na palavra secreta.")
    else:
        print(f"Putz a letra {letra} não existe na palavra secreta.")
        digitadas.pop
    
    secreto_temp = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += "*"
    
    if secreto_temp == secreto:
        print(f"Que legal você acertou!!")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temp}")

    chances -= 1

    print(f"Você ainda tem {chances} chance(s)")