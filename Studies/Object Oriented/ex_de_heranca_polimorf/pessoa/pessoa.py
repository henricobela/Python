from pessoa.corpo import Corpo


class Pessoa(Corpo):
    """
    Classe que herda outra classe Corpo, onde nela há atributos de uma pessoa.

    Metodos:
        __init__()
        __str__()
    """

    def __init__(self, nome="Zé Ninguem", idade=1200, sexo="Assexuado?"):
        """
        Este metodo define o inicio da Classe Pessoa
        que herda outra classe chamada Corpo, onde é definida pelos atributos de ambas as classes.

        Atributos:
            self.nome: uma string destinada ao nome de uma pessoa
            self.idade: um valor inteiro destinado a idade da pessoa
            self.sexo: uma string destinada a sexualidade da pessoa
            self.cabeca: herança da classe Corpo
            self.braco_direito: herança da classe Corpo
            self.braco_esquerdo: herança da classe Corpo
            self.dorso: herança da classe Corpo
            self.perna_direita: herança da classe Corpo
            self.perna_esquerda: herança da classe Corpo
        """
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
        """
        Metodo que retorna o nome da pessoa se necessario

        retorna self.nome
        """
        return self.nome
