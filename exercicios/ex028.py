import random
from time import sleep

numRand = random.randint(0, 5)

numUser = int(input('Digite seu palpite: '))

print('PROCESSANDO...')
sleep(2)

if numRand == numUser:
    print('PARABÉNS, VOCÊ ACERTOU!!!')
else:
    print('Não foi dessa vez!!!')
