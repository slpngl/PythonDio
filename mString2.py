nome = "Jandira"
idade = "37"
profissao = "dentista"
especialidade = "odontopediatria e ortodontia"
kms = 45712

##  Definindo Dicionário

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %s" %(nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {0} Idade: {1}" .format(nome, idade))
print("Nome: {0} Idade: {1} Nome: {0}" .format(nome, idade))
print("Nome: {name} Idade: {age}" .format(name=nome, age=idade))

print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade} Saldo: {kms:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {kms:10.1f}")


##Fatiamento de Strings
print(especialidade[0])
print(especialidade[-2])
print(especialidade[:9])
print(especialidade[10:])
print(especialidade[10:16])
print(especialidade[10:16:2])
print(especialidade[:])
print(especialidade[::-1])

##Strings de múltiplas linhas
mensagem = f"""
   Olá meu nome é {nome},
 E minhas especialidades são : {especialidade}.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)

