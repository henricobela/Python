meta = 10000

vendas = [
    ["Joao", 15000],
    ["Julia", 27000],
    ["Marcus", 9900],
    ["Maria", 3750],
    ["Ana", 10300],
    ["Alon", 7870],
]

contador = 0
tamanho_lista_vendas = len(vendas)

for venda in vendas:
    if venda[1] >= meta:
        contador += 1

resultado = contador / tamanho_lista_vendas

print(f"{resultado:.0%} de vendedores bateram a meta")


melhor_vendedor = ""
maior_vendas = 0

for venda in vendas:
    if venda[1] >= maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]

print(f"{melhor_vendedor} foi o melhor vendedor com {maior_vendas} vendas")
