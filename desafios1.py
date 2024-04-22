capacidade_atual, aumento_percentual = map(int, input().split())
saida = (capacidade_atual * (aumento_percentual/100)) + capacidade_atual
print(round(saida))
