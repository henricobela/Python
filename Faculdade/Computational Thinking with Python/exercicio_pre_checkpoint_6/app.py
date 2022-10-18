from functions import *


while True:
    opt = int(input("O que voce deseja fazer?\n\n[1] Cadastrar Usuario\n[2] Criar Captchas\n[0] Para Sair\n"))

    if opt == 1:
        lista = []

        while True:
            clear()
            menu()
            escolha = input("Por favor escolha uma opção: ")
            if escolha == "1":
                clear()
                nome, sobrenome, telefone, email, pais = criar()
                adicionar(nome,sobrenome,telefone,email,pais,lista)

            elif escolha == "2":
                clear()
                ler(lista)
                print("\nPressione ENTER para voltar ao MENU")
                if input():
                    pass

            elif escolha == "3":
                clear()
                email = input("Por favor digite o E-mail de seu cliente:")
                if verificar(email,lista) == True:
                    nome, sobrenome, telefone, email_alterado, pais = criar()
                    editar(email, nome, sobrenome, telefone, email_alterado, pais, lista)                
                else:
                    print("Não existe nem um cliente com esse email")
                print("\nPressione ENTER para voltar ao MENU")
                if input():
                    pass

            elif escolha == "4":
                clear()
                email = input("Por favor digite o E-mail de seu cliente:")
                excluir_ = excluir(email,lista)
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
                pesq = pesquisar(email,lista)
                if pesq != True:
                    print("Email nao encontrado")

                print("\nPressione ENTER para voltar ao MENU")
                if input():
                    pass

            elif escolha == "6":
                print("Muito obrigado por utilizar o nosso programa!!!")
                break

            else: 
                print("Por favor escolha um valor valido entre os disponiveis")  
    elif opt == 2:
        clear()
        menu_captcha()
        #digitar dps captchas
    
    elif opt != 1 and opt != 2 and opt != 0:
        clear()
        print("Digite uma opçao válida!!!")
    
    elif opt == 0:
        clear()
        print("Obrigado por utilizar os servicos!!!")
        break 
    