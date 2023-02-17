def leia_int(texto):
    while True:
        try:
            numero = int(input(texto))
        except (TypeError, ValueError):
            print('ERRO! ')
            continue
        except KeyboardInterrupt:
            print('\nO usuário não quis digitar o valor! ')
            return 0
        else:
            return numero


def linha():
    print('-' * 50)


def cabecalho(texto):
    linha()
    print(texto.center(50))
    linha()


def menu(opcoes):
    cabecalho('Menu do sistema de cadastro')
    for i, item in enumerate(opcoes):
        print(f'({i + 1}) - {item}')
    linha()

    return leia_int('Digite sua opção: ')
