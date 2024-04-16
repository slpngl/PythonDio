def escrever_arquivo(texto):
    # diretorio = 'C:/Projetos/.../pastaatual/arquivo'
    #quando voce nao passa nada ele cria no diretorio atual
    arquivo = open('notas.txt' , 'w')
    #arquivo = open(diretorio, 'w')
# se nao existir, ele cria, w -> write
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open('notas.txt' , 'a')
# se nao existir, ele cria, w -> write
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open('notas.txt', 'r')
    texto = arquivo.read()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.slpt('\n')
    for x in aluno_nota:
        lista_notas = x.slip(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4
        print (media(lista_notas))

if __name__ == '__main__':
    aluno = 'Jandira, 10 , 9 , 8 , 7'
    atualizar_arquivo('notas.txt' , aluno)
