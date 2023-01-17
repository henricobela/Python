'''
Integrantes do Sprint 2 - Grupo FeelingWhat:
    Henrico Nardelli Bela - RM 95985
    Guilherme Antonio Silva - RM 95044
    Felype Nunes De Souza - RM 96232
    Rafael Pereira da Silva - RM 94341
'''

"""
TASK: SPRINT 4 - Entregáveis


1 - Considerando o Sprint 3 devidamente criado, codifique as funcionalidades do menu em Python. Utilizando os conceitos vistos até o final do ano, como: Funções / procedimentos / listas / Duplas / Dicionários / Tabela (lista + Dicionário) / Arquivos

2 - Fazer um Pitch-vídeo (até 2 minutos) demonstrando a aplicação. 

O Sprint é uma entrega relacionada a Disciplina. Não a entrega dada ao cliente. Nesta entrega, devem ser abordados conteúdos vistos na disciplina, ou seja, a entrega não tem relação com o projeto final entregue ao cliente.

A entrega deve funcionar em ambiente local, ou seja, somente os arquivos .py devem funcionar em qualquer interpretador Python.

Usabilidade e boas práticas são habilidades importantes que devem ser empregadas em todos os projetos.
"""


"""
Link do video: https://youtu.be/DVySznibUy0
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


def dicionario_cadastro():
    cadastro = {
        "nome": "",
        "cpf": "",
        "email": "",
    }
    return cadastro


def preencher_cadastro():
    dicionario = dicionario_cadastro()
    dicionario["nome"] = input("Digite seu nome: ")
    dicionario["cpf"] = input("Digite seu cpf: ")
    dicionario["email"] = input("Digite seu email: ")

    return dicionario["nome"], dicionario["cpf"], dicionario["email"]


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
    return int(input("Em uma escala de 0 a 10, qual a chance de você recomendar a BASF para um amigo?\nDigite de 0 a 10: "))



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
            if num >= 0 and num <= 4:
                print(f"{nome} Sentimos muito pelo seu transtorno, como podemos melhorar nossos serviços?")
                comment = input("Comente aqui: ")
                break
            elif num >= 5 and num <= 7:
                print(f"{nome} Entendemos seu ponto, para podermos melhorar nossos serviços comente sobre sua experiencia?")
                comment = input("Comente aqui: ")
                break
            elif num > 7 and num <= 10:
                print(f"{nome} Agradecemos sua participação! Caso queira comentar sua experiencia, abaixo temos um campo de comentario")
                comment = input("Comente aqui: ")
                break
            elif num < 0 or num > 10:
                clear()
                print("Por favor, digite um numero de 0 a 10!")
                num = perguntar_pesquisa()
            else:
                break

    elif opcao == 5:
        if nome == "":
            print(f"Comentário deixado por zé ninguem: {comment}")
        else:
            print(f"Comentário deixado por {nome}: {comment}")
        print("SAINDO!!!")
        break