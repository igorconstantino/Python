matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite o elemento [{linha}, {coluna}]: '))

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
