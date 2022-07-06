"""
6 - O Sr. Manoel Joaquim expandiu seus negócios para além dos
negócios de 1,99 e agora possui uma loja de conveniências. Faça
um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores
referentes aos preços das mercadorias. Um valor zero deve ser
informado pelo operador para indicar o final da compra. O
programa deve então mostrar o total da compra e perguntar o
valor em dinheiro que o cliente forneceu, para então calcular e
mostrar o valor do troco. Após esta operação, o programa deverá
voltar ao ponto inicial, para registrar a próxima compra. A saída
deve ser conforme o exemplo abaixo:

Introdução a Programação

6 – Lojas Tabajara

Produto 1: R$ 2.20

Produto 2: R$ 5.80

Produto 3: R$ 1.00

Total: R$ 9.00

Dinheiro: R$ 20.00

Troco: R$ 11.00 ...
"""


while True:
    print("\nLojas Tabajara")

    print("\nDigite o preço das compras a seguir:")
    
    soma = 0
    cont = 1

    while True:
        
        try:
            valor = float(input())
            
            if valor < 0:
                raise ValueError
            
            elif valor == 0:
                print(f"Total: R${soma:.2f}")

                dineirito = float(input("Digite o valor fornecido para o pagamento: "))

                if dineirito > soma:
                    troco = dineirito - soma
                    print(f"\nTroco: {troco:.2f}")
                
                elif dineirito < soma:
                    print("Valor inválido")
                    while dineirito < soma:
                        dineirito = float(input("\nDigite o valor fornecido para o pagamento: "))
                        troco = dineirito - soma
                        print(f"Troco: {troco:.2f}")

                break  

            else:
                soma += valor
                
                print(f"Produto {cont}: R${valor:.2f}")
                cont += 1

        except ValueError:
            print("Digite um valor válido pf bro")