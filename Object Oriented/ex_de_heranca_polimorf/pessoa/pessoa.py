from pessoa.corpo import Corpo


class Pessoa(Corpo):
    
    def __init__(self, nome = "Zé Ninguem", idade = 1200, sexo = "Assexuado?"):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cabeca = Corpo.cabeca()
        self.braco_direito = Corpo.braco_direito()
        self.braco_esquerdo = Corpo.braco_esquerdo()
        self.dorso = Corpo.dorso()
        self.perna_direita = Corpo.perna_direita()
        self.perna_esquerda = Corpo.perna_esquerda()
    
    def __str__(self):
        print("Pessoa criada!")

    
