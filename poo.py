#Desafio Bicicletária

class Bicicleta:
    #pass - bloco vazio - __metodosEspeciais__ 
    def __init__(self, cor, modelo, ano, valor) : #construtor
        #atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 0

    print("Adquirindo bicicleta")

    def buzinar(self):
        print("Bibibi")

    def parar(self):
        print("Stop!")

    def coorer(self):
        print("ACELERANDO...")

    def trocar_marcha(self, nro_marcha):
        print("trocando")

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada")
            else:
                print("Não foi possivel trocar de marcha...")

# O primeiro argumento de um método é o "self", ou seja, a instancia do objeto , idependente do nome que voce coloca ali, se não
#colocar nada, o metodo nao funciona quando chamado, pq vai faltar argumento. 

# Método destrutor, não tão necessarios pois o python tem um coletor de lixo , o _del__ é utilizado quando queremos realizar uma 
# ação (operação) ao excluir a instancia .

    def __del__(self):
        print("Reciclando Bike... (removendo a instancia da classe)")

# para chamar o nmetodo destrutor (del) é só chamar a palavra reservada del 



b1 = Bicicleta("Vermelha", "caloi", 2020, 600) #objetos instanciado

b1.buzinar()
b1.coorer()
b1.parar()

#Acessando atributos
print(b1.ano, b1.cor , b1.modelo, b1.valor)

# Método que retorna o o objeto e seus devidos atributos

def __str__(self):
    return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



