print("-"*30)
print("Calculadora Simples")
print("-"*30)
print("#"*30)
print("Escolha uma operação Matemática")
print("-"*30)

a, b, resultado = 0, 0, 0
operacoes = "1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\nEscolha um numero para operação matemática: "

escolha = str(input(operacoes))

if escolha == "1":
    print(f"Você escolheu: Soma")
    a = int(input("Digite um numero a ser somado: "))
    b = int(input("Digite outro numero a ser somado: "))
    resultado = a + b
    print(f"Soma realizada: {a} + {b} = {resultado}")

elif escolha == "2":
    print(f"Você escolheu: Subtração")
    a = int(input("Digite um numero a ser subtraído: "))
    b = int(input("Digite outro numero a ser subtraído: "))
    resultado = a - b
    print(f"Subtração realizada: {a} - {b} = {resultado}")

elif escolha == "3":
    print(f"Você escolheu: Divisão")
    a = int(input("Digite um numero a ser dividido: "))
    b = int(input("Digite outro numero a ser dividido: "))
    resultado = a / b
    print(f"Dividido realizada: {a} / {b} = {resultado}")    

elif escolha == "4":
    print(f"Você escolheu: Multiplicação")
    a = int(input("Digite um numero a ser multiplicado: "))
    b = int(input("Digite outro numero a ser multiplicado: "))
    resultado = a * b
    print(f"Dividido realizada: {a} x {b} = {resultado}")   

elif escolha not in ["1", "2", "3", "4"]:
    print("Por favor, escolha uma opção válida.\n1, 2, 3 ou 4.")
