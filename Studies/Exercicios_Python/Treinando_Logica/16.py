# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 


metros_area = float(input("Por favor digite o tamanho em metros quadrados da area a ser pintada: "))
lata_tinta = 18
metros_lata_18_litros = 54
qntd_latas = 0
valor_lata = 80

if metros_area > metros_lata_18_litros:
    for i in range(int(metros_area) + 1):
        if i % metros_lata_18_litros == 0:
            qntd_latas += 1
            
    print(f"A quantidade de latas de tinta será: {qntd_latas} e o preco total a ser pago é: R$ {valor_lata * qntd_latas}")
else:
    print(f"A quantidade de latas de tinta será: {qntd_latas + 1} e o preco total a ser pago é: R$ {valor_lata}!!!")



