# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input(
    "Digite o sexo de acordo com a seguinte legenda: [F]eminino, [M]asculino: "
)

if letra.upper() == "F":
    print(f"{letra} - Feminino.")
elif letra.upper() == "M":
    print(f"{letra} - Masculino.")
else:
    print(f"{letra} Sexo inválido.")
