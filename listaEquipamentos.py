itens = []
contador = 0


while contador < 3 :
    print("Qual item deseja adicionar?")
    itens.append(input())
    contador = contador +1 
    
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")