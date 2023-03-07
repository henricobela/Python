# Faça um Programa que leia três números e mostre o maior deles.

x = []

for i in range(3):
    num = int(input(f"Digite o {i+1}o numero: "))
    x.append(num)

print(x)

aux = 0
for i in x:
    if i > aux:
        aux = i

print(f"O maior numero da lista {x}, é {aux}")
