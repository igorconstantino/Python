from random import randint

contador = 0

while True:
    par_impar_user = input('\nVocê quer par ou ímpar? [p/i]: ').strip().lower()

    num_user = int(input('Digite um número: '))
    num_pc = randint(0, 10)

    soma = num_user + num_pc

    print(f'O computador jogou {num_pc}')

    if soma % 2 == 0 and par_impar_user == 'p':
        print('PARABÉNS DEU PAR!!! Vamos de novo...')
    elif soma % 2 == 1 and par_impar_user == 'i':
        print('PARABÉNS DEU ÍMPAR!!! Vamos de novo...')
    else:
        print('Você errou, que pena...')
        break

    contador += 1
    print(f'Você já acertou um total de {contador} vezes!')
