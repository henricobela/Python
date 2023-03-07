"""
    Nome: Henrico Nardelli Bela
    RM: 95985
    Turma: 1TIAR
"""
import random


def cortar_string(*args):
    for sentence in args:
        word_list = []
        word = ""
        for ch in sentence:
            if ch == " " and word != "":
                word_list.append(word)
                word = ""
            else:
                word += ch
        if word != "" and word != " ":
            word_list.append(word)
    return [i for i in word_list if i != " "]


def contar_palavras(lista_string):
    return len(lista_string)


def mediaDinamica(*args):
    soma = 0
    for cont in range(0, len(args), 1):
        soma += args[cont]
        media = soma / len(args)
    return media


def verificar_maior(*args):
    verificador = 0
    for arg in args:
        verificador = arg
        if arg > verificador:
            verificador = arg

    return verificador


def verificar_cpf(cpf):
    if len(cpf) != 9:
        print(f"CPF Invalido, tamanho nao corresponde: {len(cpf)}\n")
    else:
        print(f"CPF Válido, tamanho corresponde: {len(cpf)}\n")


def criar_cpf_aleatorio():
    return random.randint(10000000000, 99999999999)


def menu():
    print(
        "Seja bem vind(o/a) ao programa!!!\n\n"
        + "1 - Contar palavras\n"
        + "2 - Verificar Validade CPF\n"
        + "3 - Ver 2 digitos correspondentes\n"
        + "4 - Gerar um CPF aleatório\n"
        + "5 - Calcular Media\n"
        + "6 - Verificar Maior valor\n"
        + "0 - Sair\n"
    )


################### PROGRAMA PRINCIPAL ##############################


while True:
    menu()
    opcao = int(input())
    if opcao == 1:
        print(cortar_string("ola!!!", "     tudo", "!!!bem"))
        print(
            "Certo, vamos contar as palavras, agora digite as palavras que deseja contar: "
        )
        frase = cortar_string(input())
        cont = contar_palavras(frase)
        print(frase, cont)

    elif opcao == 2:
        print("Certo, vamos verificar o CPF, digite os 9 digitos: ")
        cpf = input()
        verificar_cpf(cpf)

    elif opcao == 3:
        print(f"CPF: {cpf}, ultimos 2 digitos: {cpf[-2:]}")

    elif opcao == 4:
        cpf_aleatorio = criar_cpf_aleatorio()
        print(f"CPF Gerado: {cpf_aleatorio}")

    elif opcao == 5:
        print(f"Media: {mediaDinamica(6, 6)}")

    elif opcao == 6:
        print(f"Maior Numero: {verificar_maior(8, 5 , 6, 111)}")

    elif opcao == 0:
        print("SAINDO!!!")
        break
