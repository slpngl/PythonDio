class Pessoa:
    def __init__(self, nome, idade= None):
        self.nome = nome 
        self.idade = idade 

    @classmethod
    def criar_deDataNascimento(cls, ano, nome):
        idade = 2024 - ano
        return cls(nome, idade)

p = Pessoa.criar_deDataNascimento(1992, "Jandira")
