# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato. 

x = []

for i in range(3):
    valor_produto = float(input(f"Digite o valor do {i+1}o produto: "))
    x.append(valor_produto)

valor_mais_barato = 10000000000

for i in x:
    if i < valor_mais_barato:
        valor_mais_barato = i

for i in range(len(x)):
    if x[i] == valor_mais_barato:
        print(f"Voce deve comprar o produto {x[i]}, por ser mais barato")

