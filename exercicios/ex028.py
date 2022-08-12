import random
numRand = random.randint(0, 5)

numUser = int(input('Digite seu palpite: '))
if numRand == numUser:
    print('PARABÉNS!!!')
else:
    print('Não foi dessa vez!!!')
