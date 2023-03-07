# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58


altura = float(input("Digite sua altura: "))
peso_ideal = (72.7 * altura) - 58

print(f"O peso ideal para uma pessoa que tem altura de: {altura}, é: {peso_ideal}")
