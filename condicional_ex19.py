"""
19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula 
entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

while True:

    try:
        num = int(input("\nDigite um número inteiro para saber suas casas decimais: "))
        
        if num < 0 or num > 9999:
            raise ValueError
        
        else:
            num = str(num) 
            qtd = len(num)

            if qtd == 1:
                dig0 = int(num[0]) // 1 
                
                print(f"{num} = {dig0} unidade(s)")

            elif qtd == 2:
                dig0 = int(num[0]) // 1 
                dig1 = int(num[1]) // 1 

                print(f"{num} = {dig0} dezena(s) e {dig1} unidade(s)")

            elif qtd == 3:
                dig0 = int(num[0]) // 1 
                dig1 = int(num[1]) // 1 
                dig2 = int(num[2]) // 1 


                print(f"{num} = {dig0} centena(s), {dig1} dezena(s) e {dig2} unidade(s)")

            elif qtd == 4:
                dig0 = int(num[0]) // 1 
                dig1 = int(num[1]) // 1 
                dig2 = int(num[2]) //1 
                dig3 = int(num[3]) // 1 

                print(f"{num} = {dig0} milhar(es), {dig1} centena(s), {dig2} dezena(s) e {dig3} unidade(s)")
            
    except ValueError:
        print("Valor inválido. Coloque um número inteiro!")

    except TypeError:
        pass
