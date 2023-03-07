preco = 1500
custo = 400
lucro = 800


def calcular_carga_tributo(valor_preco, valor_custo, valor_lucro):
    imposto = valor_preco - valor_custo - valor_lucro
    return imposto / valor_preco


print(f"Valor da carga: {calcular_carga_tributo(preco, custo, lucro):.1%}")
print(f"Valor da nova carga: {calcular_carga_tributo(6000, 500, 1200):.2%}")
