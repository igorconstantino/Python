while True:
    print('========== SISTEMA DE AJUDA PYHELP ==========')
    opcao = input('Digite o comando que deseja saber (digite "fim" para terminar): ').strip().lower()
    if opcao == 'fim':
        break
    help(opcao)
