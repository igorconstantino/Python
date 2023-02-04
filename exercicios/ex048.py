print('Soma dos números ímpares, múltiplos de 3, no intervalo de 1 a 500')

soma = 0
for i in range(1, 500):
    if i % 3 == 0 and i % 2 == 1:
        soma += i

print(soma)
