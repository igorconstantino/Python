import random
from time import sleep

num_rand = 0
num_user = 1
contador = 0

while num_rand != num_user:
    num_rand = random.randint(0, 10)
    num_user = int(input('\nDigite seu palpite: '))
    contador += 1

    print('PROCESSANDO...')
    sleep(1)

    if num_rand == num_user:
        print('\nPARABÉNS, VOCÊ ACERTOU!!!')
        print(f'Foram necessárias {contador} tentativas.')
    else:
        print('Não foi dessa vez!!!')
