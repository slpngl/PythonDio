contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['rato', 'gato', 'pato']
print(contador_letras(lista_animais))

soma = lambda a,b : a+b

#dicionario
calculadora = {
    'soma' : lambda a, b: a+b,
    'subtração' : lambda a, b: a-b,
    'multiplicação' : lambda a, b: a*b,
    'divisao' : lambda a, b: a/b
} 

print(type(calculadora))
soma =calculadora['soma'] #acessando o dicionario, o valor soma. 
# é a mesma coisa se fizesse isso soma =  lambda a, b: a+b
print('A soma é {}' .format(soma(10,5)))