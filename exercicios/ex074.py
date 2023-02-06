from random import randint

menor = maior = 0

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for i in range(len(numeros)):
    if i == 0:
        menor = maior = numeros[0]
    else:
        if numeros[i] < menor:
            menor = numeros[i]
        if numeros[i] > maior:
            maior = numeros[i]

print(f'Os números gerados são: {numeros}')
print(f'O maior número é {maior} e o menor é {menor}')
