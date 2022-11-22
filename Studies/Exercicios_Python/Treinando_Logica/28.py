# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 

periodo = input("Digite o periodo que voce estuda, M-matutino ou V-Vespertino ou N-Noturno: ")

if periodo.upper() == "M":
    print("Bom dia!")
elif periodo.upper() == "V":
    print("Boa tarde!")
elif periodo.upper() == "N":
    print("Boa noite!")
else:
    print("Periodo invalido")