'''
Integrantes do Sprint 2 - Grupo FeelingWhat:
    Henrico Nardelli Bela - RM 95985
    Guilherme Antonio Silva - RM 95044
    Felype Nunes De Souza - RM 96232
    Rafael Pereira da Silva - RM 94341
'''

"""
TASK: 1 - Considerando o Sprint 2 devidamente criado, 
escolha e codifique ao menos 3 funcionalidades do menu, 
utilizando os conceitos aprendidos: Funções / procedimentos / listas.
"""


def clear():
    return print("\n" * 125)


def menu():
    print("\nPor favor digite um dos numeros abaixo: \n"
          "[1] - Preencher Cadastro\n" + 
          "[2] - Ver Cadastro\n" + 
          "[3] - Excluir Cadastro\n" + 
          "[4] - Prosseguir para pesquisa de satisfação\n" + 
          "[5] - SAIR")


def preencher_cadastro():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    email = input("Digite seu email: ")
    return nome, cpf, email


def ver_cadastro(nome, cpf, email):
    print("-"*20)
    print(f"Cadastro de {nome}")
    print("-"*20)
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Email: {email}")


def excluir_cadastro():
    nome = ""
    cpf = ""
    email = ""
    return nome, cpf, email


def perguntar_pesquisa():
    return int(input("Em uma escala de 0 a 10, qual a chance de você recomendar a BASF para um amigo?"))



############################################## - PRINCIPAL - ########################################

nome = ""

print("------------------------\n" + 
        "PROGRAMA DE SATISFAÇÃO\n" + 
        "------------------------\n" + 
        "Somos a Feeling What?!!!\n" + 
        "Gostaríamos de pedir algumas informações antes de começarmos com a pesquisa!\n")
while True:
    menu()
    opcao = int(input())
    clear()
    if opcao == 1:
        nome, cpf, email = preencher_cadastro()
        while True:
            if "@" not in email:
                clear()
                print(f"Email {email} invalido! Por favor, digite um email valido")
                email = input("Digite novamente seu email: ")
            else:
                print("Email valido, siga em frente")
                break
    elif opcao == 2:
        try: 
            ver_cadastro(nome, cpf, email)
        except:
            print("Cadastro inexistente! Por favor, preencher seu cadastro!!!")
    elif opcao == 3:
        nome, cpf, email = excluir_cadastro()
        print("Cadastro excluido com sucesso!")
    elif opcao == 4:
        clear()
        print("Indo para pesquisa...")
        num = perguntar_pesquisa()
        comment = "Sem comentários"
        while True:
            if num >= 0:
                print(f"{nome} Sentimos muito pelo seu transtorno, como podemos melhorar nossos serviços?")
                comment = input("Comente aqui: ")
                print(f"Comentário deixado: {comment}")
                print("SAINDO!!!")
                break
            elif num <= 5:
                print(f"{nome} Entendemos seu ponto, para podermos melhorar nossos serviços comente sobre sua experiencia?")
                comment = input("Comente aqui: ")
                print(f"Comentário deixado: {comment}")
                print("SAINDO!!!")
                break
            elif num >= 6 and num <= 10:
                print(f"{nome} Agradecemos sua participação! Caso queira comentar sua experiencia, abaixo temos um campo de comentario")
                comment = input("Comente aqui: ")
                print(f"Comentário deixado: {comment}")
                print("SAINDO!!!")
                break
            elif num < 0 or num > 10:
                clear()
                print("Por favor, digite um numero de 0 a 10!")
                num = perguntar_pesquisa()
            else:
                break
    elif opcao == 5:
        print(f"Comentário deixado: {comment}")
        print("SAINDO!!!")
        break