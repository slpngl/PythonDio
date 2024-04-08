
# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
def recomendar_plano (consumo):
    if  0 < consumo <= 10 :
        return "Plano Essencial Fibra - 50Mbps"
    if  11 < consumo <= 20 :
        return  "Plano Prata Fibra - 100Mbps"
    if  consumo >= 20 :
       return  "Plano Premium Fibra - 300Mbps"


print(recomendar_plano(consumo))

