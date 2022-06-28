vendas_produtos = [
    ("iphone", 555888, 214555),
    ("samsung", 55888, 21555),
    ("xiaomi", 5888, 2555),
]

lista_vendas2019 = []

for produto, vendas2019, vendas2020 in vendas_produtos:
    lista_vendas2019.append(vendas2019)

print(lista_vendas2019)

print("-"*20)

lista_vendas2020 = [vendas2020 for produto, vendas2019, vendas2020 in vendas_produtos]
print(lista_vendas2020)

print("-"*20)

maior_venda_2020 = max([(vendas2020, produto) for produto, vendas2019, vendas2020 in vendas_produtos])
print(f"O produto mais vendido no ano de 2020 foi {maior_venda_2020[1]}, " 
      f"com {maior_venda_2020[0]} vendas.")

print("-"*20)

meta = 1000
vendas_produtos_2 = [1500, 150, 200, 3000]
produtos = ["vinho", "macarrao", "feijao", "carne"] 

lista_vendas2019_2 = [produto for i, produto in enumerate(produtos) if vendas_produtos_2[i] > meta]
print(lista_vendas2019_2)

print("-"*20)

meta = 2000
vendedores_dicionario = {
    "Ana": 1900,
    "Marcos": 2000,
    "Stenio": 8000,
}

bonus = [(vendedores_dicionario[item] * 0.1) if vendedores_dicionario[item] > meta else 0 for item in vendedores_dicionario]
print(bonus)