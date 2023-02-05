primeiro_termo = int(input('Digite o primerio termo da sua P.A.: '))
razao = int(input('Digite a razão da sua P.A.: '))
i = 0
a_n = primeiro_termo

while i < 10:
    print(a_n, end=' ')
    a_n += razao
    i += 1
