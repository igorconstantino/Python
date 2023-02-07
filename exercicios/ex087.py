matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

soma_pares = 0
soma_3coluna = 0
maior_2linha = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite o elemento [{linha}, {coluna}]: '))

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

        if coluna == 2:
            soma_3coluna += matriz[linha][coluna]

        if linha == 1 and coluna == 0:
            maior_2linha = matriz[linha][coluna]
        elif linha == 1 and matriz[linha][coluna] > maior_2linha:
            maior_2linha = matriz[linha][coluna]

    print()

print('=-' * 30)
print(f'A soma dos números pares é {soma_pares}')
print(f'A soma da 3° coluna é {soma_3coluna}')
print(f'O maior da 2° linha é {maior_2linha}')
