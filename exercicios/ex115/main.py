from lib.interface import *
from lib.arquivo import *

nome_arquivo = 'pessoas.txt'

if not existe_arquivo(nome_arquivo):
    criar_arquivo(nome_arquivo)

while True:
    opcao = menu(['Cadastrar pessoa', 'Verificar lista', 'Sair do sistema'])

    if opcao == 1:
        cabecalho('Cadastrar pessoa')
        nome = input('Digite o nome: ').strip().title()
        idade = leia_int('Digite a idade: ')
        cadastrar(nome_arquivo, nome, idade)

    elif opcao == 2:
        cabecalho('Verificar lista')
        ler_arquivo(nome_arquivo)

    elif opcao == 3:
        cabecalho('Obrigado por utilizar nosso sistema!')
        break

    else:
        print('OPÇÃO INVÁLIDA!')
