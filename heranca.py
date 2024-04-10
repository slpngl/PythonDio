#Herança simples    

class Veiculo:
    def __init__(self, cor, placa, numero_rodas) :        
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado):
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}")

moto = Motocicleta("preta","mto0101", 2)
print(moto)
moto.ligar_motor()

carro = Carro("azul" , "car0102", 4)

caminhao =  Caminhao("roxo" , "trk0103", 8)

carro.ligar_motor()
caminhao.esta_carregado()

