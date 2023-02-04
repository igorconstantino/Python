primeiro_termo = int(input('Digite o primerio termo da sua P.A.: '))
razao = int(input('Digite a razão da sua P.A.: '))

for i in range(primeiro_termo, primeiro_termo + (9 * razao) + 1, razao):
    print(i)
