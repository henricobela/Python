# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


metros_area = float(
    input("Por favor digite o tamanho em metros quadrados da area a ser pintada: ")
)
lata_tinta = 18
metros_lata_18_litros = 108
qntd_latas = 0
valor_lata = 80

galao_tinta = 3.6
metros_galao_litros = 21.6
galao_valor = 25
qntd_galao = 0


if metros_area > metros_lata_18_litros:
    for i in range(int(metros_area) + 1):
        if i % metros_lata_18_litros == 0 or i % metros_galao_litros == 0:
            qntd_latas += 1
            qntd_galao += 1

    print(
        f"A quantidade de latas de tinta será: {qntd_latas} e o preco total a ser pago é: R$ {valor_lata * qntd_latas}"
    )
    print(
        f"A quantidade de galoes de tinta será: {qntd_galao} e o preco total a ser pago é: R$ {galao_valor * qntd_galao}"
    )
else:
    print(
        f"A quantidade de latas de tinta será: {qntd_latas + 1} e o preco total a ser pago é: R$ {valor_lata}!!!"
    )
    print(
        f"A quantidade de galoes de tinta será: {qntd_galao + 1} e o preco total a ser pago é: R$ {galao_valor * qntd_galao}"
    )
