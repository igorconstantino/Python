def leia_int(texto):
    while True:
        numero = input(texto)
        if numero.isnumeric():
            numero = int(numero)
            return numero
        else:
            print('ERRO!', end=' ')


# Main
n = leia_int('Digite um número inteiro: ')
print(f'Você acabou de digitar {n}')
