class Estudante:
    #essa é uma váriavel de classe - se alterar aqui troca para todas as instâncias criadas
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula}  - {self.escola} "
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

a1 = Estudante("Guilherme", 12345)
a2 = Estudante("Giovana", 56789)

print(a1)
print(a2)

a1.matricula = 828282

mostrar_valores(a1, a2)

a1.escola = "Python"

mostrar_valores(a1,a2)

Estudante.escola = "Mudou"

mostrar_valores(a1,a2)
