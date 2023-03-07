# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arq = int(input("Digite o tamanho do arquivo em MB: "))
velocidade_link = int(input("Digite a velocidade de download em Mbps: "))

tempo_medio = (tamanho_arq / velocidade_link) / 60

print(
    f"Para um arquivo de tamanho: {tamanho_arq} MB, com uma velocidade de internet de: {velocidade_link} Mbps, o tempo medio para download é de: {tempo_medio:.2f} minutos"
)
