from random import randint
from time import sleep

MAX_NUM = 6
lista = []
sorteio = []

quantidade = int(input('Quantos jogos você quer sortear? '))

for i in range(quantidade):
    j = 0
    while j < MAX_NUM:
        num = randint(0, 60)

        if num not in sorteio:
            sorteio.append(num)
            j += 1
    sorteio.sort()
    lista.append(sorteio[:])
    sorteio.clear()

for i, sorteio in enumerate(lista):
    print(f'O sorteio {i + 1} foi: {sorteio}')
    sleep(0.5)
