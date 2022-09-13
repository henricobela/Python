"""
    Nome: Henrico Nardelli Bela
    RM: 95985
    Turma: 1TIAR
"""
import random


#funcao para receber os parametros do usuario (ainda com bug para contar quantas palavras na frase)
#sem usar o metodo split :) to tentando professor rsrrs
def contar_palavras1(*args):
    word = ""
    count = 0
    puncts = "!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    for letra in range(0, len(args), 1):
        if letra != " ":
            word += args[letra]
            for w in word:
                if w not in puncts:
                    count += 1
    return word, count


def contar_palavras2(*args):
    word = ""
    count = 0
    for palavra in range(0, len(args), 1):
        word += args[palavra] + " "
        count += 1

    return word, count


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
        "Seja bem vind(o/a) ao programa!!!\n\n" + 
        "1 - Contar palavras\n" +
        "2 - Verificar Validade CPF\n" +
        "3 - Ver 2 digitos correspondentes\n" + 
        "4 - Gerar um CPF aleatório\n" + 
        "5 - Calcular Media\n" + 
        "6 - Verificar Maior valor\n" + 
        "0 - Sair\n")


################### PROGRAMA PRINCIPAL ##############################


while True:
    menu()
    opcao = int(input())
    if opcao == 1:
        print(contar_palavras2("ola!!!", "     tudo", "!!!bem")) #esse funciona!!!
        print("Certo, vamos contar as palavras, agora digite as palavras que deseja contar: ")
        print(contar_palavras1(input()))
    
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



