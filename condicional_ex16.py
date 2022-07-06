"""
16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa
deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir 
os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""

print("\nBem vindo \n")

while True:
    a = int(input("Digite o valor de a: "))

    if a == 0 :
        print("\nO valor de a não pode ser 0.\n")

    elif a != 0:
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))

        delta = b**2 - 4 * a * c


        if delta < 0:
            print("\nA equação não possui raízes reais.")

        elif delta == 0:
            x = ((b * -1) + delta**0.5) / 2 * a
            print("\nA equação possui apenas uma raiz real. X é igual a", x)

        elif delta > 0:
            x1 = ((b * -1) + delta**0.5) / 2 * a
            x2 = ((b * -1) - delta**0.5) / 2 * a

            print(f"\nX1 é igual a {x1} e X2 é igual a {x2}")
