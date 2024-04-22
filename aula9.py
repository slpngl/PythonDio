def escrever_arquivo(texto):
    # diretorio = 'C:/Projetos/.../pastaatual/arquivo'
    #quando voce nao passa nada ele cria no diretorio atual
    arquivo = open('teste.txt' , 'w')
    #arquivo = open(diretorio, 'w')
# se nao existir, ele cria, w -> write
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('teste.txt' , 'a')
# se nao existir, ele cria, w -> write
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')

