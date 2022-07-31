
"""
9. A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa 
que gere a série até que o valor seja maior que 500
"""

ultimo = 1
penultimo = 1

print(ultimo)
print(penultimo)

for i in range(1000):
        
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        
        if ultimo > 500:
            break
        
        print(termo)
