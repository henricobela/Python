"""
INTEGRANTES

NOME: HENRICO NARDELLI BELA 
RM: 95985

NOME: FELYPE NUNES 
RM: 96232

"""


from functions import *

menu_principal = "Menu Principal"
opt_menu_princ = "Digite a opção desejada: "


clear()
while True:
    opt = input(
        f"{menu_principal: ^50}\n\n\t[1] Cadastrar Usuario\n\t[2] Captchas\n\t[0] Para Sair\n\n{opt_menu_princ: >40}"
    )

    if opt == "1":
        lista = []

        while True:
            clear()
            menu()
            escolha = input("Por favor escolha uma opção: ")
            if escolha == "1":
                clear()
                nome, sobrenome, telefone, email, pais = criar()
                adicionar(nome, sobrenome, telefone, email, pais, lista)

            elif escolha == "2":
                clear()
                ler(lista)
                print("\nPressione ENTER para voltar ao MENU")
                if input():
                    pass

            elif escolha == "3":
                clear()
                email = input("Por favor digite o E-mail de seu cliente:")
                if verificar(email, lista) == True:
                    nome, sobrenome, telefone, email_alterado, pais = criar()
                    editar(
                        email, nome, sobrenome, telefone, email_alterado, pais, lista
                    )
                else:
                    print("Não existe nem um cliente com esse email")
                print("\nPressione ENTER para voltar ao MENU")
                if input():
                    pass

            elif escolha == "4":
                clear()
                email = input("Por favor digite o E-mail de seu cliente:")
                excluir_ = excluir(email, lista)
                if excluir_ == True:
                    print("Cliente excluido com sucesso")
                else:
                    print("E-mail não existe na base de dados clientes")

                print("\nPressione ENTER para voltar ao MENU")
                if input():
                    pass

            elif escolha == "5":
                clear()
                email = input("Por favor digite o E-mail de seu cliente:")
                pesq = pesquisar(email, lista)
                if pesq != True:
                    print("Email nao encontrado")

                print("\nPressione ENTER para voltar ao MENU")
                if input():
                    pass

            elif escolha == "6":
                print("Muito obrigado por utilizar o nosso programa!!!\n\n")
                break

            elif (
                escolha != "1"
                and escolha != "2"
                and escolha != "3"
                and escolha != "4"
                and escolha != "5"
                and escolha != "6"
            ):
                print("Por favor escolha um valor valido entre os disponiveis\n")
                input()

    elif opt == "2":
        lista = []
        while True:
            clear()
            menu_captcha()
            opt_captcha = input("Digite a opção desejada: ")
            if opt_captcha == "1":
                x = captcha(size=10)
                print(f"\nEste foi o captcha gerado: {x}\n")
                input("Digite ENTER para voltar ao menu dos Captchas")
            elif opt_captcha == "2":
                s = int(
                    input(
                        "Digite a quantidade de caracteres desejados em seu catpcha (Ex. 15): "
                    )
                )
                x = captcha(size=s)
                print(f"\nEste foi o captcha gerado: {x}\n")
                input("Digite ENTER para voltar ao menu dos Captchas")
            elif opt_captcha == "3":
                s = int(input("Captcha com quantos caracteres? "))
                menu_captcha_dinamico()
                cap_din_opt = input("Escolha (Ex. le / Ld / ed): ")
                x = captcha_dinamico(s, cap_din_opt)
                print(f"\nEste foi o captcha gerado: {x}\n")
                input("Digite ENTER para voltar ao menu dos Captchas")
            elif opt_captcha == "4":
                s = int(input("Captcha com quantos caracteres? "))
                menu_captcha_dinamico()
                cap_din_opt = input("Escolha (Ex. le / Ld / ed): ")
                for i in range(10):
                    x = captcha_dinamico(s, cap_din_opt)
                    lista.append(x)
                print(f"\nEstes foram os captchas gerados: {lista}\n")
                input("Digite ENTER para voltar ao menu dos Captchas")
            elif opt_captcha == "5":
                if len(lista) == 0:
                    print(
                        "Lista de Captchas não criada, favor criar no menu 4 Captchas\n"
                    )
                else:
                    x = v5(lista)
                    print(f"\nLista de Captchas: \n\n{x}")
                input("Digite ENTER para voltar ao menu dos Captchas")
            elif opt_captcha == "0":
                print("Obrigado por criar os captchas")
                break

    elif opt != "1" and opt != "2" and opt != "0":
        clear()
        print("\tDigite uma opçao válida!!!\n")

    elif opt == "0":
        clear()
        print("\tObrigado por utilizar os servicos!!!\n")
        break
