

def menu():
    print("-"*30)
    print("Calculadora Simples")
    print("-"*30)
    print("1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n0 - Sair")


a, b, resultado, continuar = 0, 0, 0, True

while continuar != False:
    menu()
    escolha = str(input("Escolha um numero para operação matemática: "))

    if escolha == "1":
        print(f"Você escolheu: Soma")
        a = int(input("Digite um numero a ser somado: "))
        b = int(input("Digite outro numero a ser somado: "))
        resultado = a + b
        print(f"Soma realizada: {a} + {b} = {resultado}")
        manter_ligada = str(input("Deseja manter a calculadora ligada e continuar as operações? [S]im ou [N]ão: "))
        if manter_ligada == "S":
            continue
        elif manter_ligada == "N":
            continuar = False

    elif escolha == "2":
        print(f"Você escolheu: Subtração")
        a = int(input("Digite um numero a ser subtraído: "))
        b = int(input("Digite outro numero a ser subtraído: "))
        resultado = a - b
        print(f"Subtração realizada: {a} - {b} = {resultado}")
        manter_ligada = str(input("Deseja manter a calculadora ligada e continuar as operações? [S]im ou [N]ão: "))
        if manter_ligada == "S":
            continue
        elif manter_ligada == "N":
            continuar = False

    elif escolha == "3":
        print(f"Você escolheu: Divisão")
        a = int(input("Digite um numero a ser dividido: "))
        b = int(input("Digite outro numero a ser dividido: "))
        resultado = a / b
        print(f"Dividido realizada: {a} / {b} = {resultado}")    
        manter_ligada = str(input("Deseja manter a calculadora ligada e continuar as operações? [S]im ou [N]ão: "))
        if manter_ligada == "S":
            continue
        elif manter_ligada == "N":
            continuar = False

    elif escolha == "4":
        print(f"Você escolheu: Multiplicação")
        a = int(input("Digite um numero a ser multiplicado: "))
        b = int(input("Digite outro numero a ser multiplicado: "))
        resultado = a * b
        print(f"Dividido realizada: {a} x {b} = {resultado}")   
        manter_ligada = str(input("Deseja manter a calculadora ligada e continuar as operações? [S]im ou [N]ão: "))
        if manter_ligada == "S":
            continue
        elif manter_ligada == "N":
            continuar = False

    elif escolha == "0":
        print("Saindo da calculadora...")
        continuar = False

    elif escolha not in ["1", "2", "3", "4", "0"]:
        print("Por favor, escolha uma opção válida.\n1, 2, 3, 4 ou 0.")

