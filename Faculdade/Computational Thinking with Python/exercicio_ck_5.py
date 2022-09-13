"""
    Nome: Henrico Nardelli Bela
    RM: 95985
    Turma: 1TIAR
"""
import random


# EXERCÍCIOS:
# 1. Contar palavras
#         Testes:
#         Olá, bom dia (3)
#         Olá,bom.dia(3)
#         Olá,                bom.dia (3)
# 2. Dados 9 digitos do numero do CPF, verificar se ele é ou não válido
# 3. Dados 9 digitos do numero do CPF, apresentar os 2 dígitos correspondentes
# 4. Gerar um CPF aleatório
#     from random import randint
#     numero = str(randint(100000000, 999999999))
# 5. Utilizando parâmetros dinâmicos, faça uma função que calcule a média dos argumentos
# 6. Utilizando parâmetros dinâmicos, retornar o maior valor


def contar_palavras(*args):
    word = ""
    count = 0
    for palavra in range(0, len(args), 1):
        word += " " + args[palavra]
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
        print(contar_palavras("ola", "tudo", "bem"))
    
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



