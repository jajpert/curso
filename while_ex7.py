"""
7 – Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final 
da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais 
alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos 
dos clientes
"""


while True:
    print("\nAcademia Tabajara")

    m_baixo = 1000
    m_alto = 0
    m_gordo = 0
    m_magro = 1000
    
    soma_p = 0
    soma_a = 0
    cont = 0

    while True:
        
        codigo = input("\nDigite seu código: ")

        if codigo == "0":
            media_p = soma_p / cont
            media_a = soma_a / cont

            print(f"\nO cliente mais magro é {cod_magro} que pesa {m_magro} e mede {alt_magro}.")
            print(f"\nO cliente mais gordo é {cod_gordo} que pesa {m_gordo} e mede {alt_gordo}.")
            print(f"\nO cliente mais alto é {cod_alto} que mede {m_alto} e pesa {peso_alto}")
            print(f"\nO cliente mais baixo é {cod_baixo} que mede {m_baixo} e pesa {peso_baixo}")
            print("\nA média de altura da academia é", media_a)
            print("\nA média de peso da academia é", media_p)

            break
            
        try:
            peso = float(input("Digite seu peso: "))
            altura = float(input("Digite sua altura: "))

            if peso < 0 or altura < 0:
                raise ValueError

            else:
                soma_p += peso
                soma_a += altura
                cont += 1

        except ValueError:
            print("Valor inválido né coisa fofa")
            continue

        if peso < m_magro:
            m_magro = peso
            cod_magro = codigo
            alt_magro = altura
        
        elif peso > m_gordo:
            m_gordo = peso
            cod_gordo = codigo
            alt_gordo = altura

        if altura < m_baixo:
            m_baixo = altura
            cod_baixo = codigo
            peso_baixo = peso

        elif altura > m_alto:
            m_alto = altura
            cod_alto = codigo
            peso_alto = peso

    break