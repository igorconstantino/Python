from random import randint
from time import sleep


def sortear(lista):
    for i in range(5):
        lista.append(randint(0, 10))
    for elemento in lista:
        sleep(0.5)
        print(elemento, end=' ')
    print('FIM!')


def somar_pares(lista):
    soma = 0
    for elemento in lista:
        if elemento % 2 == 0:
            soma += elemento
    print(f'A soma dos pares é {soma}')


sorteados = []

sortear(sorteados)
somar_pares(sorteados)
