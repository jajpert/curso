"""
Se o parâmetro da função for divisível por 3, retorne Fizz, se o parâmetro
da função for divisivel por 5, retorne Buzz. Se o parâmetro for divisivel por 5 e 3, retorne
FizzBuzz, caso contrário, retorne o número enviado.
"""

def div(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"

    return "Esse número não é divisivel por 5 e nem por 3"

number = int(input("Digite um número a seguir: "))
print(div(number))