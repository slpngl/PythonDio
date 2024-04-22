lista = [1 , 10]
try :
   # divisao = 10/0
   # numero = lista[3]
   # x = a 
   print("Começooo")
except IndexError:
    #print("Nao é possivel dividir por 0")
    print("Nao possui esse indice")
except ZeroDivisionError:
    print("Nao é possivel dividir por 0")
except BaseException as ex:
    print("erro desconhecido!! Erro {}".format(ex))
else:
    print("executa quando nao dá erro")
finally:
    print("sempre executa, apesar dos erros , e se deu certo ou não")

    #BaseException é a classe pai de todas as excessoes 