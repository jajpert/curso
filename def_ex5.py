"""
5 - Faça um programa que use a função valorPagamento para determinar o
valor a ser pago por uma prestação de uma conta. O programa deverá solicitar
ao usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e
devolverá este valor ao programa que a chamou. O programa deverá então
exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a
pedir outro valor de prestação e assim continuar até que seja informado um
valor igual a zero para a prestação. Neste momento o programa deverá ser
encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total
de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando
houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


valor_prestacao = float(input("Digite o valor da prestação: "))

while valor_prestacao != 0:

    dias_atraso = int(input("Digite o número de dias em atraso: "))
    print()

    def valorPagamento(valor_prestacao, dias_atraso):
        if dias_atraso == 0:
            print(f"O valor do pagamento é R${valor_prestacao}")

        elif dias_atraso > 0:
            multa = valor_prestacao * 0.03
            valor = dias_atraso * (0.1 / 100)
            total = valor + multa + valor_prestacao
            print(f"O valor do pagamento é R${total:.2f}")


    valorPagamento(valor_prestacao, dias_atraso)

    valor_prestacao = float(input("\nDigite o valor da prestação: "))