"""
Criando um cnpj
"""

from random import randint

def cria_cnpj():
    novo_cnpj = []
    for n in range(8):
        x = randint(0, 9)
        novo_cnpj.append(x)

    lista = [0, 0, 0, 1]
    for i in lista:
        novo_cnpj.append(i)

    return novo_cnpj

cnpj = cria_cnpj()

def primeiro_dig(cnpj):
    pedaco_cnpj = cnpj[:4]
    pedaco_cnpj2 = cnpj[4:12]

    j = 5
    soma = 0
    for i in pedaco_cnpj:
        i = int(i)
        soma += i * j
        j -= 1

    l = 9
    for k in pedaco_cnpj2:
        k = int(k)
        soma += k * l
        l -= 1

    pri_dig = 11 - (soma % 11)

    if pri_dig > 9:
        pri_dig = 0
        cnpj.append(pri_dig)
    else:
        cnpj.append(pri_dig)


def segundo_dig(cnpj):
    pedaco_cnpj = cnpj[:5]
    pedaco_cnpj2 = cnpj[5:13]

    j = 6
    soma = 0
    for i in pedaco_cnpj:
        i = int(i)
        soma += i * j
        j -= 1

    l = 9
    for k in pedaco_cnpj2:
        k = int(k)
        soma += k * l
        l -= 1

    seg_dig = 11 - (soma % 11)
    
    if seg_dig > 9:
        seg_dig = 0
        cnpj.append(seg_dig)
    else:
        cnpj.append(seg_dig)

primeiro_dig(cnpj)
segundo_dig(cnpj)

novo_cnpj = []
for num in cnpj:
    num = str(num)
    novo_cnpj.append(num)

s = ""
print(s.join(novo_cnpj))