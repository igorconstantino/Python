def existe_arquivo(nome_arquivo):
    try:
        file = open(nome_arquivo, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo):
    try:
        file = open(nome_arquivo, 'wt+')
        file.close()
    except FileNotFoundError:
        print('Erro na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso')


def ler_arquivo(nome_arquivo):
    try:
        file = open(nome_arquivo, 'rt')
    except FileNotFoundError:
        print('Erro ao ler arquivo!')
    else:
        for linha in file:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        file.close()


def cadastrar(nome_arquivo, nome, idade):
    try:
        file = open(nome_arquivo, 'at')
    except FileNotFoundError:
        print('Erro ao abir arquivo!')
    else:
        file.write(f'{nome};{idade}\n')
        print(f'{nome} cadastrado com sucesso!')
