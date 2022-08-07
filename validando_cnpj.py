"""
5432 98765432 -> primeiro digito -> formula -> 11 - (soma da mult % 11) = p.d. 
65432 98765432 -> segundo digito -> formula -> 11 - (soma da mult % 11) = s.d. 
(se o digito for maior que 9, ele se torna 0)
se o cnpj formado for igual ao digitado o cnpj é válido
"""

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

    return pri_dig

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

    return seg_dig


print("Entre com o cnpj: ")
cnpj = []

while True:
    cnpj_em_string = input()
    for char in cnpj_em_string:
        if char.isdigit():
            cnpj.append(int(char))

    if len(cnpj) != 14:
        print("Entre um numero válido para ser verificado!")
        cnpj.clear()
        print("Entre com o cnpj: ")
    else:
        break

pri = primeiro_dig(cnpj)
seg = segundo_dig(cnpj)

if pri == cnpj[12] and seg == cnpj[13]:
    print("\nEste cnpj é válido")

else:
    print("\nEste cnpj não é válido")