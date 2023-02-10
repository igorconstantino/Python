from time import sleep


def contador(inicio, fim, passo):
    if inicio > fim and passo > 0:
        passo -= passo * 2
    if passo == 0:
        if inicio > fim:
            passo = -1
        elif fim > inicio:
            passo = 1
    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(i, end=' ')
    print(' FIM')


contador(1, 10, 1)
contador(10, 0, 2)

inicio_user = int(input('Digite o início: '))
fim_user = int(input('Digite o fim: '))
passo_user = int(input('Digite o passo: '))

contador(inicio_user, fim_user, passo_user)
