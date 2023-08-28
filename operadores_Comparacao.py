## (2/5) Operadores comparação

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque) #saldo maior que saq
print(saldo >= saque) #saldo maior ou igual que saq
print(saldo < saque) #saldo menor que saq
print(saldo <= saque)  #saldo menor ou igual que saq

## (3/5) Operadores atribuição

saldo = 500 #atribuição simples
print(saldo)

saldo += 10 #atribuição com adição (ele mesmo +10)
print(saldo)

saldo -= 5 #atribuição com subtração (ele mesmo -5)
print(saldo)

saldo //= 2 #divisão retornando so o valor inteiro (subscreve o valor)
print(saldo)

saldo /= 2 #divisão (retorna float)
print(saldo)

saldo *= 10 #ele mesmo multiplicado 10
print(saldo)

saldo = 500
saldo %= 4
print(saldo)

saldo = 500
saldo **= 2 # exponenciação
print(saldo)