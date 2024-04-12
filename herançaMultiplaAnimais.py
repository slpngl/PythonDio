class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    #método formatação da string 
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, corPelo, **kw):
        self.corPelo = corPelo
        super().__init__(**kw)
    #super puxa argumentos da classe mae, **keyargs

class Ave(Animal):
    def __init__(self,cordoBico, **kw):
        self.cordoBico = cordoBico
        super().__init__(**kw)


class Cachorro(Mamifero):
    pass
#Não tem nenhuma caracteristica adicional, então não foi mexido nesse método

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cordoBico, corPelo, nro_patas):
        #Método super "manual", não usando o **kw, mas é necessario a passagem de todos os parametros
        super().__init__(corPelo=corPelo, cordoBico= cordoBico, nro_patas=nro_patas)
        #print(ornitorrinco._mro__) print(ornitorrinco.mro()) ordem que o copilador le os atributos 

cao = Cachorro(corPelo="Preto" , nro_patas = 4)
print(cao)


ornitorrinco = Ornitorrinco(nro_patas=2, corPelo="vermelho", cordoBico="laranja")
print(ornitorrinco)

#Herança multipla em django, função mixin e vai encorporando comportamentos especificos dentro da classe  