# Faça um Programa que leia três números e mostre-os em ordem decrescente. 

x = []

for i in range(3):
    n = int(input(f"Digite o {i+1}o numero: "))
    x.append(n)

y = x.copy()

for travado in range(0, len(x), 1):
    for proximo in range(travado + 1, len(x), 1):
        if x[travado] < x[proximo]:
            aux = x[travado]
            x[travado] = x[proximo]
            x[proximo] = aux

# ou usar o metodo sort de lista
# y.sort()

print(f"Numeros digitados: {y}, em ordem decrescente: {x}")