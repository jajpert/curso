"""
29- Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
"""

i = int(input("Digite quantos termos a série terá: "))

h = 1
H = 0
for n in range(1, i + 1):
    print(f"{h}/{n}", end = "")

    if n < i:
        print(" + ", end = "")
    
    else:
        print(".")

    H += h / n

print(f"A soma da série deu {H:.2f}")    