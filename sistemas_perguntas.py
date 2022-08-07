"""
Sistema de perguntas e respostas
"""

perguntas = {
    "Pergunta 1" : {
        "pergunta" : "Quanto é 2 + 2? ",
        "respostas" : {
            "a" : "2",
            "b" : "4",
            "c" : "9",
        },
        "resposta certa" : "b",
    },
    "Pergunta 2" : {
        "pergunta" : "Quanto é 5 + 2? ",
        "respostas" : {
            "a" : "2",
            "b" : "9",
            "c" : "7",
        },
        "resposta certa" : "c",
    },
    "Pergunta 3" : {
        "pergunta" : "Quanto é 34 + 1? ",
        "respostas" : {
            "a" : "35",
            "b" : "34",
            "c" : "33",
        },
        "resposta certa" : "a",
    },
    "Pergunta 4" : {
        "pergunta" : "Quanto é 5 * 2? ",
        "respostas" : {
            "a" : "3",
            "b" : "10",
            "c" : "5",
        },
        "resposta certa" : "b",
    },
    "Pergunta 5" : {
        "pergunta" : "Quanto é 10 - 3? ",
        "respostas" : {
            "a" : "12",
            "b" : "10",
            "c" : "7",
        },
        "resposta certa" : "c",
    },
}

respostas_certas = 0
for pergunta_key, pergunta_value in perguntas.items():
    
    print(f"{pergunta_key} : {pergunta_value['pergunta']}")

    print("Respostas")
    for reposta_key, respota_value in pergunta_value["respostas"]. items():
        print(f"[{reposta_key}] : {respota_value}")

    escolha = input("Sua resposta: ")

    if escolha == pergunta_value["resposta certa"]:
        print("Boaaaa ta certin")
        respostas_certas += 1

    else:
        print("Puxa vc errou")
    print()


qtd_perguntas = len(perguntas)
porcentagem = respostas_certas / qtd_perguntas * 100
print(f"Você acertou {porcentagem}% das perguntas, ou seja, {respostas_certas} resposta(s) certa(s).")
