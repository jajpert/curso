"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer
    opção de refazer
"""

lista = []
tarefa_desfeita = []

while True:

    titulo = "Menu"
    print()
    print(titulo.center(50, "_"))
    print()

    print("1- Adicionar tarefa")
    print("2- Listar tarefas")
    print("3- Opção de desfazer")
    print("4- Opção de refazer")
    print("5- Sair")


    try:
        decisao = int(input("\nEscolha o que deseja fazer: "))
        print()
        
        if decisao < 1 or decisao > 5:
            raise ValueError
        
        if decisao == 5:
            print("Você saiu")
            break

        elif decisao == 1:
            print("Adicionar tarefa")

            tarefa = input("Digite a tarefa: ")
            lista.append(tarefa)

        elif decisao == 2:
            print("Listar tarefas")

            if not lista:
                print("Nenhuma tarefa para listar")

            else:
                print(lista)

        elif decisao == 3:
            print("Desfazer")

            if not lista:
                print("Nenhuma tarefa para desfazer")

            else:
                print(f"A ação {lista[-1]} desfeita")
                tarefa_desfeita.append(lista[-1])
                del lista[-1]

        elif decisao == 4:
            print("Refazer")

            if not tarefa_desfeita:
                print("Sem tarefa para refazer")

            else:
                lista.append(tarefa_desfeita[-1])
                del tarefa_desfeita[-1]

                if not tarefa_desfeita:
                    print("Todas as tarefas foram refeitas")    
                else:
                    print(tarefa_desfeita[-1], "foi refeita")

    except ValueError:
        print("Valor inválido")