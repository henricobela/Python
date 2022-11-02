from pessoa.pessoa import Pessoa


ALGUEM = Pessoa(nome = "Henrico Bela", idade = 26, sexo = "Masculino")

print(nome := ALGUEM.nome)
print(idade := ALGUEM.idade)
print(sexo := ALGUEM.sexo)

print(f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}")

corpo = [
    ALGUEM.cabeca, 
    ALGUEM.braco_direito, 
    ALGUEM.braco_esquerdo, 
    ALGUEM.dorso, 
    ALGUEM.perna_direita, 
    ALGUEM.perna_esquerda
    ]

for i in corpo:
    print(i)

print("###############################################")

OUTRO_ALGUEM = Pessoa()

OUTRO_ALGUEM.nome = input("Qual seu nome? ")
OUTRO_ALGUEM.idade = input("Qual sua idade? ")
OUTRO_ALGUEM.sexo = input("Qual seu sexo? ")

print(outro_nome := OUTRO_ALGUEM.nome)
print(outro_idade := OUTRO_ALGUEM.idade)
print(outro_sexo := OUTRO_ALGUEM.sexo)

print(f"Nome: {outro_nome}\nIdade: {outro_idade}\nSexo: {outro_sexo}")

outro_corpo = [
    OUTRO_ALGUEM.cabeca, 
    OUTRO_ALGUEM.braco_direito, 
    OUTRO_ALGUEM.braco_esquerdo, 
    OUTRO_ALGUEM.dorso, 
    OUTRO_ALGUEM.perna_direita, 
    OUTRO_ALGUEM.perna_esquerda
    ]

for i in outro_corpo:
    print(i)