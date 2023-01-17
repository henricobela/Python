from pessoa.pessoa import Pessoa                                                # trazendo a classe Pessoa criada para o programa principal


ALGUEM = Pessoa(nome = "Henrico Bela", idade = 26, sexo = "Masculino")          # criando um objeto da classe Pessoa, e dando um nome, idade, e sexo a esta pessoa

print(nome := ALGUEM.nome)                                                      # deste modo, a criaçao e atribuiçao de variaveis fica mais dinamica
print(idade := ALGUEM.idade)                                                    # e pode ser utilizada mais adiante do codigo. 
print(sexo := ALGUEM.sexo)                                                      # Ex. (variavel := valor) ----- (nome := 'Henrico')
                                                                                # E de quebra ja pode ser usada para printar na tela por exemplo
print(f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}")                            # printando o nome, idade e sexo

corpo = [                                                                       # definindo a lista de elementos que um corpo de uma pessoa tem
    ALGUEM.cabeca, 
    ALGUEM.braco_direito, 
    ALGUEM.braco_esquerdo, 
    ALGUEM.dorso, 
    ALGUEM.perna_direita, 
    ALGUEM.perna_esquerda
    ]

for i in corpo:                                                                 # iterando sobre essa lista criada
    print(i)                                                                    # printando cada elemento da lista

print("###############################################")                        # print pra separar td

OUTRO_ALGUEM = Pessoa()                                                         # criando outro objeto da mesma classe Pessoa

OUTRO_ALGUEM.nome = input("Qual seu nome? ")                                    # agora ao inves de definir na classe, é perguntado para o usuario o nome idade e sexo
OUTRO_ALGUEM.idade = input("Qual sua idade? ")
OUTRO_ALGUEM.sexo = input("Qual seu sexo? ")

print(outro_nome := OUTRO_ALGUEM.nome)                                          # definindo as novas variaveis de nome, idade e sexo, e printando as mesmas
print(outro_idade := OUTRO_ALGUEM.idade)
print(outro_sexo := OUTRO_ALGUEM.sexo)

print(f"Nome: {outro_nome}\nIdade: {outro_idade}\nSexo: {outro_sexo}")          # print mais organizado das variaveis criadas acima

outro_corpo = [                                                                 # outra lista criada, com os mesmos tipos de elementos de um corpo
    OUTRO_ALGUEM.cabeca, 
    OUTRO_ALGUEM.braco_direito, 
    OUTRO_ALGUEM.braco_esquerdo, 
    OUTRO_ALGUEM.dorso, 
    OUTRO_ALGUEM.perna_direita, 
    OUTRO_ALGUEM.perna_esquerda
    ]

for i in outro_corpo:                                                           # iterando sobre essa lista nova
    print(i)                                                                    # printando cada elemento dessa nova lista