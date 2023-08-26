

def menu():
    print("-"*30)
    print("Calculadora Simples")
    print("-"*30)
    print("1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n0 - Sair")


def limpar_tela():
    print("\n"*100)


def msg_saida():
    print("Saindo da calculadora...")


def pegar_numeros():
    nums = []
    soma_cont = True

    while soma_cont == True:
        num = str(input()).upper()
        if num == "SAIR":
            soma_cont = False
        else:
            nums.append(num)
            soma_cont = True
    return nums



def soma():
    resultado = 0
    print("Digite os numeros que deseja somar, digite SAIR para parar de somar. Obs: Pressione Enter para inserir outro numero para a soma.")
    nums = pegar_numeros() #implementar nas outras funcoes
    for num in nums:
        resultado += int(num)
    return resultado, nums


def subtracao():
    nums = []
    sub_cont = True
    resultado = 0
    print("Digite os numeros que deseja subtrair, digite SAIR para parar de subtrair. Obs: Pressione Enter para inserir outro numero para a subtração.")
    while sub_cont == True:
        num = str(input()).upper()
        if num == "SAIR":
            sub_cont = False
        else:
            nums.append(num)
            sub_cont = True

    for num in nums:
        resultado -= int(num)

    return resultado, nums


def divisao():
    nums = []
    div_cont = True
    resultado = 1
    print("Digite os numeros que deseja dividir, digite SAIR para parar de dividir. Obs: Pressione Enter para inserir outro numero para a divisão.")
    while div_cont == True:
        num = str(input()).upper()
        if num == "SAIR":
            div_cont = False
        else:
            nums.append(num)
            div_cont = True

    for num in nums:
        resultado /= int(num)

    return resultado, nums  


def multiplicacao():
    nums = []
    mult_cont = True
    resultado = 1
    print("Digite os numeros que deseja multiplicar, digite SAIR para parar de multiplicar. Obs: Pressione Enter para inserir outro numero para a multiplicação.")
    while mult_cont == True:
        num = str(input()).upper()
        if num == "SAIR":
            mult_cont = False
        else:
            nums.append(num)
            mult_cont = True

    for num in nums:
        resultado *= int(num)

    return resultado, nums 


def manter_rodando():
    manter_ligada = str(input("Deseja manter a calculadora ligada e continuar as operações? [S]im ou [N]ão: ")).upper()
    if manter_ligada == "S":
        return True
    elif manter_ligada == "N":
        msg_saida()
        return False


while True:
    menu()
    escolha = str(input("Escolha um numero para operação matemática: "))

    if escolha == "1":
        limpar_tela()
        resultado, numeros_soma = soma()
        print("Numeros somados:", *numeros_soma, " = " f"{resultado}")
        if manter_rodando() == False: break
        
    elif escolha == "2":
        limpar_tela()
        resultado, numeros_sub = subtracao()
        print("Numeros subtraídos:", *numeros_sub, " = " f"{resultado}")
        if manter_rodando() == False: break

    elif escolha == "3":
        limpar_tela()
        resultado, numeros_div = divisao()
        print("Numeros divididos:", *numeros_div, " = " f"{resultado}")
        if manter_rodando() == False: break

    elif escolha == "4":
        limpar_tela()
        resultado, numeros_mult = multiplicacao()
        print("Numeros multiplicados:", *numeros_mult, " = " f"{resultado}")
        if manter_rodando() == False: break

    elif escolha == "0":
        limpar_tela()
        msg_saida()
        break

    elif escolha not in ["1", "2", "3", "4", "0"]:
        limpar_tela()
        print("Por favor, escolha uma opção válida.\n1, 2, 3, 4 ou 0.")

