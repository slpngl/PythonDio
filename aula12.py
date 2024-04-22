import requests 

def retorna_dadosCep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    #Aqui da pra colocar a url passada tambem , {?}
    #print(response.status_code)
    #print(response.text)
    print(response.json)
    dados_cep = response.json()
    print(dados_cep['logradouro'])

# def retorna_dadosPokemon(pokemon):
#    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/')
#    dadosPokemon = response.json()
#    return dadosPokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__== '__main__' :
    retorna_dadosCep(int(input()))
    response = retorna_response('www.therow.com')

   # dadosPokemon = retorna_dadosPokemon('pikachu')

