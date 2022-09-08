'''
Integrantes do Sprint 2 - Grupo FeelingWhat:
    Henrico Nardelli Bela - RM 95985
    Guilherme Antonio Silva - RM 95044
    Felype Nunes De Souza - RM 96232
    Rafael Pereira da Silva - RM 94341
    Lais Cristina Leme da Silva - RM 94660
'''

'''
Task:
Implementação em Python de um menu listando todas as funcionalidade do sistema. 

Observe que ao escolher uma opção, o programa deverá mostrar na tela a opção 
selecionada e exibir novamente o menu com todas as funcionalidades do sistema.

ENTREGÁVEL: Arquivo .py (Implementação em Python)
'''

############################################### - INICIO - ###############################################

chatbot = "FeelingWhat ChatBot"
opcao_menu_inicio = 0
opcao_menu_bot = 0

menu_inicio = '''
----------------------\n
PESQUISA DE SATISFAÇÃO\n
----------------------\n
Deseja iniciar a pesquisa de satisfação?\n
[1] - SIM\n
[2] - NÃO\n
'''
menu_bot = f'''
----------------------\n
{chatbot}\n
----------------------\n
Olá, sou o {chatbot}, espero que esteja bem!\n
Por favor, digite o numero correspondente a opção que deseja:\n
[1] - Perguntas de Satisfação
[2] - Sair
'''

while opcao_menu_inicio != 2:
    opcao_menu_inicio = int(input(menu_inicio))

    print(f"\n{chatbot}: Voce optou pela opção {opcao_menu_inicio}\n")


    if opcao_menu_inicio == 1:
        opcao_menu_bot = int(input(menu_bot))

        print(f"{chatbot}: Voce escolheu a opção {opcao_menu_bot}\n")

        escala = int(input(f"{chatbot}: Em uma escala de 0 a 5, sendo 0 totalmente insatisfeito,\n "
                           f"e 5 totalmente satisfeito, "
                           f"como voce se sentiu com sua primeira compra de produtos da BASF?\n"))

        if escala == 0:
            print(f"Você digitou {escala}\n")
            print(f"{chatbot}: Muito obrigado, que pena :( "
                  f"Deixe uma sugestão para que possamos melhorar nosso atendimento!\n")

        elif escala > 0 and escala < 5:
            print(f"Você digitou {escala}\n")
            print(f"{chatbot}: Muito obrigado, espero que na proxima compra possamos melhor lhe atender\n")

        elif escala == 5:
            print(f"Você digitou {escala}\n")
            print(f"{chatbot}: Muito obrigado!\n")
        else:
            print(f"{chatbot}: Por favor digite uma opção entre 0 e 5")

    else:
        print("Por favor digite um numero valido, 1 ou 2.\n")

