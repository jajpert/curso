"""
3 - Faça um Programa que verifique se uma letra
digitada é "F“, "M“ ou “O”. Conforme a letra
escrever: F - Feminino, M - Masculino, O – Outros
ou Sexo Inválido.
"""

letra = input("Escreva uma letra que defina seu sexo (F, M, O): ")

letra = letra.lower()

if letra == "f":
    print("F - Feminino")

elif letra == "m":
    print("M - Masculino")

elif letra == "o":
    print("O - Outro")

else:
    print("Valor inválido")
