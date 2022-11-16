# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9). 

f = int(input("Digite os graus em Fahrenheit: "))
c = 5 * ((f-32) / 9)

print(f"Os graus em Fahrenheit {f}, convertido em Celsius são: {c:.2f}")