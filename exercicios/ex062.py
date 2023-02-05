i = 0
op = 1

primeiro_termo = int(input('Digite o primerio termo da sua P.A.: '))
razao = int(input('Digite a razão da sua P.A.: '))
a_n = primeiro_termo

while i < 10:
    print(a_n, end=' ')
    a_n += razao
    i += 1

while op != 0:
    i = 0
    op = int(input('\nVocê quer mostrar mais quantos termos? '))
    while i < op:
        print(a_n, end=' ')
        a_n += razao
        i += 1
