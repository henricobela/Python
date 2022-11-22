# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

vogais = ["a", "e", "i", "o", "u"]
letra = input("Digite uma letra: ")

if letra in vogais:
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} é consoante")