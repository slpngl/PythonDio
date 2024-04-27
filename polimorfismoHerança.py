class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

def plano_voo(obj):
    obj.voar()

#o objeto tem que ter o voar() implementado


class Aviao(Passaro):
    def voar(self):
        print("Avião está voando")

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(Aviao())