# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo. 


n_i_1 = int(input("Digite o primeiro numero inteiro: "))
n_i_2 = int(input("Digite o segundo numero inteiro: "))
n_r_1 = float(input("Digite o primeiro numero real: "))

produto = (n_i_1 * 2) * (n_i_2 / 2)
soma = (n_i_1 * 3) + n_r_1
cubo_3o = n_r_1 ** 3

print(f"O produto do dobro de {n_i_1} com metade de { n_i_2} é {produto}")
print(f"A soma do triplo de {n_i_1} com o terceiro {n_r_1} é {soma}")
print(f"{n_r_1} elevado ao cubo é {cubo_3o:.2f}")