meses = [
    "jan",
    "fev",
    "mar",
    "mai",
    "abr",
    "jun",
    "jul",
    "ago",
    "set",
    "out",
    "nov",
    "dez",
]

vendas_1sem = [25000, 29000, 22000, 17500, 15800, 19900]
vendas_2sem = [19800, 20120, 17540, 15555, 49051, 9850]

vendas_ano = vendas_1sem + vendas_2sem

print(max(vendas_ano))
print(min(vendas_ano))


i_maior = vendas_ano.index(max(vendas_ano))
i_menor = vendas_ano.index(min(vendas_ano))

print(i_maior)
print(i_menor)

print(f"O mes com o maior valor foi {meses[i_maior]} com {vendas_ano[i_maior]} vendas")

fat_total = sum(vendas_ano)

print(f"Faturamento total: R${fat_total:.2f}")

percentual = max(vendas_ano) / fat_total

print(f"Percentual: {percentual:.2f}%")

print(vendas_ano)

top3 = []

maior_valor = max(vendas_ano)
vendas_ano.remove(maior_valor)
top3.append(maior_valor)
print(top3)

maior_valor = max(vendas_ano)
vendas_ano.remove(maior_valor)
top3.append(maior_valor)
print(top3)

maior_valor = max(vendas_ano)
vendas_ano.remove(maior_valor)
top3.append(maior_valor)
print(top3)
