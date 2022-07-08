"""
10- 
"""

print("\n      Almoxarifado")
print("\nCódigo           Produto")
print("  10             caderno")
print("  20             caneta")
print("  30             lápis")
print("  40             borracha")
print("  50             régua")
print()

cad = int(input("\nDigite a quantidade de cadernos: "))
can = int(input("Digite a quantidade de canetas: "))
lap = int(input("Digite a quantidade de lápis: "))
bor = int(input("Digite a quantidade de borrachas: "))
reg = int(input("Digite a quantidade de réguas: "))
print()

while True:
    print("\nEscolha a operação:")
    print("E - Entrada no estoque")
    print("S - Saída no estoque")
    print("R - Relatório")
    print("X - Sair")
    print()

    escolha = input()
    print()
    escolha = escolha.lower()

    if escolha == "e":
        cod = int(input("\nDigite o código do produto que entrará: "))
        qtd = int(input("Digite a quantidade do produto: "))

        if cod == 10:
            cad += qtd
        
        elif cod == 20:
            can += qtd

        elif cod == 30:
            lap += qtd

        elif cod == 40:
            bor += qtd

        elif cod == 50:
            reg += qtd
        
        else:
            print("\nValor inválido")

    elif escolha == "s":
        cod = int(input("Digite o código do produto que entrará: "))
        qtd = int(input("Digite a quantidade que será retirada do produto: "))

        if cod == 10:
            
            if qtd > cad:
                print("Quantidade menor que a disponível em estoque")
            
            else:
                cad -= qtd
        
        elif cod == 20:
            
            if qtd > can:
                print("Quantidade menor que a disponível em estoque")
            
            else:
                can -= qtd

        elif cod == 30:
            
            if qtd > lap:
                print("Quantidade menor que a disponível em estoque")
            
            else:
                lap -= qtd

        elif cod == 40:
            
            if qtd > bor:
                print("Quantidade menor que a disponível em estoque")
            
            else:
                bor -= qtd

        elif cod == 50:
            
            if qtd > reg:
                print("Quantidade menor que a disponível em estoque")
            
            else:
                reg -= qtd

        else:
            print("Valor inválido")

    elif escolha == "r":
        print("Relatório")
        print()

        print(f"Há em estoque {cad} caderno(s)")
        print(f"Há em estoque {can} caneta(s)")
        print(f"Há em estoque {lap} lápis")
        print(f"Há em estoque {bor} borracha(s)")
        print(f"Há em estoque {reg} régua(s)\n")

    elif escolha == "x":
        print("\nVocê saiu\n")
        break

    else:
        print("Escolha inválida \n")