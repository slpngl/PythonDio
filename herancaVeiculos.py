#Herança simples    

class Veiculo:
    def __init__(self, cor, placa, numero_rodas) :        
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")
     
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta","mto0101", 2)
print(moto)
moto.ligar_motor()

carro = Carro("azul" , "car0102", 4)

c1 =  Caminhao("roxo" , "trk0103", 8, False)
c2 =  Caminhao("laranja" , "trk0203", 8, True)


carro.ligar_motor()
c1.esta_carregado()

print(carro)
print(c1)
print(c2)