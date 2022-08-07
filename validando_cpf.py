"""
Algoritmo para validar um cpf

O cálculo do cpf é baseado nos 2 últimos dígito
Para validar pegue os nove primeiros dígitos do cpf, gere os dois dígitos e salve em
um novo cpf.
Compare se o cpf enviado é igual ao cpf gerado
Se verdadeiro, o cpf é válido, caso contrário inválido.

Obter o primeiro dígito:
    1- Multiplicar os primeiros 9 dígitos do cpf por uma contagem regressiva
iniciando em 10 e terminando em 2.
    2- Somar todos os valores das multiplicações do passo 1.
    3- Obter o resto da divisão entre a soma e 11.
    4- Subtrair o resultado por 11.
    5- Se o resultado for maior do que 9, o dígito é 0, caso contrário,
o dígito é o resultado do passo 4.

Obter o segundo dígito:
    1- Multiplicar os 9, mais o obtido anteriormente, dígitos do cpf por uma contagem regressiva iniciando em 
11 e terminando em 2.
    2- Mesma lógica do passo 2 do primeiro dígito em diante. 

"""
cpf = []
print("Digite seu cpf a seguir:")

while True:
    cpf_em_string = input()
    for caracter in cpf_em_string:
        if caracter.isdigit():
            cpf.append(int(caracter))

    if len(cpf) != 11:
        print("Entre um numero válido para ser verificado!")
        cpf.clear()
    else:
        break

i = 10
j = 0
soma = 0
while i != 1:
    soma += cpf[j] * i

    j += 1
    i -= 1

soma %= 11
soma = abs(soma - 11)

if soma > 9:
    prim_dig = 0 
else:
    prim_dig = soma

h = 11
m = 0
som_a = 0
while h > 2:
    som_a += int(cpf[m]) * h

    m += 1
    h -= 1

som_a += prim_dig * 2
som_a %= 11
subtr = abs(som_a - 11)

if subtr > 9:
    seg_dig = 0 
else:
    seg_dig = subtr


if int(cpf[9]) == prim_dig and int(cpf[10]) == seg_dig:
    print("Esse cpf é válido!")
else:
    print("Esse cpf é inválido!")
