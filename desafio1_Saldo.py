def depositar(saldo_atual,valor_deposito):
    saldo_atual = (saldo_atual + valor_deposito)
    print("Deposito realizado com sucesso ")
    print(f"Seu saldo atual é {saldo_atual:.1f}")
    return saldo_atual

def retirar(saldo_atual, valor_retirada):
    if(valor_retirada > saldo_atual):
        print("Saldo insuficiente")
        print(f"Seu saldo atual é {saldo_atual:.1f}")
        return saldo_atual

    else:
        saldo_atual = (saldo_atual - valor_retirada)
        print("Retirada realizado com sucesso ")
        print(f"Seu saldo atual é {saldo_atual:.1f}")
        return saldo_atual

print("Seja Bem-Vindo ")
saldo_atual = float(input("Qual é o saldo atual da conta?"))
print(f"Seu saldo atual é {saldo_atual:.1f}")

valor_deposito = float(input("Qual é o valor que deseja depositar?"))

saldo_atual = depositar(saldo_atual,valor_deposito)

valor_retirada = float(input("Qual é o valor que deseja sacar?"))

saldo_atual = retirar(saldo_atual, valor_retirada)




