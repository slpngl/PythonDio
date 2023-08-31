
valor = input("Qual valor deseja sacar?")

def sacar (valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado")
    else:
        print("Não possui limite disponivel")
    

    print("Obrigada por usar")


sacar(100)
