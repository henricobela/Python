"""

Nomes: Henrico Nardelli Bela / Felype Nunes
RM: 95985, 96232

"""


def menu():
    print(
        "CADASTRO DISCIPLINAS\n" +
        "--------------------\n" +
        "0 - SAIR\n" +
        "1 - Cadastrar as disciplinas\n" +
        "2 - Listar o registro Completo\n"
    )


def menu_opcao_1():
    print("CADASTRAR COM AS NOTAS\n" +
          "-----------------------------\n" +
          "CADASTRAR DISCIPLINAS DESEJADAS. DIGITAR '.' PARA FINALIZAR\n")

def menu_opcao_2():
    print("LISTANDO O REGISTRO\n")
    print("\tDISCIPLINAS      MF    STATUS")
    print("\t-----------------------------------")


def clear():
    print("\n"*125)


def verificar_status(nota):
    return "Reprovado" if nota < 6 else "Aprovado"


def preencher_estrutura(disciplina, media, status):
    estrutura = [
        {"Disciplina": disciplina,
        "Média Anual": media,
        "status": status}
    ]
    return estrutura

#
# def verificar_maior_len(lista):
#     x = 0
#     l = []
#     for i in lista:
#         for j in i:
#             x = len(j['Disciplina'])
#             l.append(x)
#     for i in l:
#         if i > x:
#             x = i
#     return x




############################################ - PRINCIPAL - ############################################



lista = []

while True:
    menu()
    opcao = int(input("Opção desejada: "))
    clear()
    if opcao == 1:
        menu_opcao_1()
        while True:
            disciplina = input("Disciplina..........: ")
            if disciplina == ".":
                clear()
                break
            media = float(input("Média Anual........: "))
            status = verificar_status(media)
            print(f"Status........: {status}")
            lista_dict = preencher_estrutura(disciplina, media, status)
            lista.append(lista_dict)
            print()
    elif opcao == 2:
        menu_opcao_2()
        for i in lista:
            for j in i:
                print(f"\t{j['Disciplina']}" +
                      f"| {j['Média Anual']}" +
                      f"| {j['status']}")
        print()
    elif opcao == 0:
        print("SAINDO!!!")
        break