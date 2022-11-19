# João Papo-de-Pescador, homem de bem, 
# comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido 
# pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas. 


peso_limite = 50
preco_excedente = 4.0
multa = 0
peso_peixe = int(input("Digite o peso dos peixes: "))

if peso_peixe > peso_limite:
    excesso = peso_peixe - peso_limite
    for i in range(excesso):
        multa += preco_excedente

    print(f"O preco a ser pago com multa é de: {multa}")
else:
    print(f"Nao foi excedido o peso limite para os peixes! Peso: {peso_peixe}, peso limite: {peso_limite}")