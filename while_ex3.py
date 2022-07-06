"""
3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm` ou "o";
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite seu nome: ")
while len(nome) <= 3:
	nome = input("Informe um nome válido: ")

idade = int(input("Digite sua idade: "))
while idade >= 150 or idade <= 0:
    idade = int(input("Informe uma idade válida: "))


salario = float(input("Digite seu salário: "))
while salario < 0:
    salario = float(input("Digite um salário válido: "))

sexo = input("Digite seu sexo (f, m ou o): ").lower()
while sexo != "f" and sexo != "m" and sexo != "o":
    sexo = str(input("Digite um sexo válido: "))

es = input("Digite seu estado civil: ").lower()
while es != "s" and es != "c" and es != "v" and es != "d":
    es = input("Digite um estado civil válido: ")