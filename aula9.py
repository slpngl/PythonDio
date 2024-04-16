def escrever_arquivo(texto):
    arquivo = open('teste.txt' , 'w')
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

