class Error(Exception): #Essa classe exception ,
#e é obritadoria a criançao dessa classe error quando for criar
#a sua propria classe de excessão, nesse caso a InputError
#por convenção tambem, toda classe de erro termina com Error. 
    pass

class InputError(Error):
    #criação do construtor:
    def __init__(self, mensagem):
        self.mensagem = mensagem



while True:
    try:
        x = int(input("Entre com o n de 0 a 10"))
        print(x)
        if x>10:
            raise InputError("Numero não pode ser maior que 10!")
        #forçar uma excessão
        elif x<0:
            raise InputError("Número não pode ser menor que 0")
        break 
        #força saida do loop , nesse caso a unica saida. 
    except ValueError:
        print("Valor invalido, só numeros!")
    except InputError as ex:
        print(ex)