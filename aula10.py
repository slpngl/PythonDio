from datetime import date , time, datetime , timedelta

def trabalhando_com_Date():
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    # mostra data formatada do jeito que passar
    print(data_atual.strftime('%A %B %Y'))
    #se atribuir ela a  uma variavel, vira string. data_atual é do tipo Date(), 
    #tendo funções possiveis p manipula-la

def trabalhando_com_Time():
    horario =time(hour=15 , min=5 , second=30)
    print(horario.strftime('%H %M %S'))
    print(type(horario))
    
def trabalhando_com_dateTime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%c'))
    print(data_atual.year)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    #ele pega o indice do dia da semana na função weekday e associa com a tupla, 
    #pois estao no mesmo formato (segunda=0 / domingo =6)
    data_criada = datetime(2020, 5, 15, 8, 30, 20)
    print(data_criada)
    data_string = '01/01/2024'
    data_convertida = datetime.strftime(data_string, '%d/%m/%y')
    print(data_convertida)
#Usando o import timedelta
    nova_data = data_convertida - timedelta(days=365 , hours=2 , minutes=15)
#tirou menos um ano, 2h, 15min
    print(nova_data)
    nova_data = data_convertida + timedelta(days=365 , hours=2 , minutes=15)




if __name__ == '__main__':
    trabalhando_com_dateTime()

# mostra data formatada do jeito que passar