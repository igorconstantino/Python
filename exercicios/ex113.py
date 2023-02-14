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


# Main
n = leia_int('Digite um número inteiro: ')
print(f'Você acabou de digitar {n}')
