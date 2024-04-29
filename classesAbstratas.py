#criando classes abstratas - abc : abstract base class
#@abstractmethod 
from abc import ABC, abstractmethod #abstractproperty

class ControleRemoto(ABC):
    @abstractmethod  
    def ligar(self):
        pass
        
    @abstractmethod     
    def desligar(self):
        pass

    @property
    #@abstractproperty - entrou em desuso, so o propriety + abstract method. 
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
#sou obrigada a implementar os metodos da classe mae aqui:
    def ligar(self):
        print("Ligando a tv...")
    def desligar(self):
        print("Desligando a tv...")
    @property
    def marca(self):
        return "LG"


class ControlePortao(ControleRemoto):
    def ligar(self):
        print("Abrindo o portão")
    def desligar(self):
        print("Fechando o portão")
    @property
    def marca(self):
        return "Dufrio"


controleTV = ControleTV()
controleTV.ligar()
controledoPortao = ControlePortao()
controledoPortao.desligar()
print(ControlePortao.marca)
print(controleTV.marca)