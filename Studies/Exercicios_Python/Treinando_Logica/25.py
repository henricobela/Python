# Faça um Programa que leia três números e mostre o maior e o menor deles.

x = []

for i in range(3):
    num = int(input(f"Digite o {i+1}o numero: "))
    x.append(num)

print(x)

maior = 0
for i in x:
    if i > maior:
        maior = i

print(f"O maior numero da lista {x}, é {maior}")

menor = 1000000
for i in range(len(x)):
    if x[i] < menor:
        menor = x[i]

print(f"O menor numero da lista {x}, é {menor}")
