'''
Projete e implemente um programa para ler
o valor do credito pre-existente e a duracao de uma chamada entao calcular o valor
da chamada, valor dos impostos, o valor total da chamada e o saldo existente apos
a ligacao.
'''

def teto(duracao:float)->int:
	if duracao - int(duracao) == 0:
		return duracao
	
	else:
		return int(duracao) + 1

def piso(duracao:float)->int:
	return int(duracao)

def arredonda(duracao:float)->int:
	if duracao - int(duracao) < 0.5:
		return int(duracao)
	
	else:
		return int(duracao) + 1

quantas_vezes = int(input())

for _ in range(quantas_vezes):
	credito_pre = float(input())
	duracao = float(input())

	valor_chamada = teto(duracao) * 1.55
	impostos = 0.185 * valor_chamada
	valor_total = valor_chamada + impostos
	credito_final = credito_pre - valor_total

	print(f"Valor da Chamada            :R${valor_chamada:7.2f}")
	print(f"Valor dos Impostos          :R${impostos:7.2f}")
	print(f"Valor Total da Chamada      :R${valor_total:7.2f}")
	print(f"Valor do Saldo Remanescente :R${credito_final:7.2f}")
	print()
	