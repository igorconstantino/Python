registros = []
pessoa = []
menor = maior = 0

while True:
    nome = input('Digite o nome da pessoa: ').strip()
    peso = float(input('Digite o peso da pessoa: '))

    pessoa.append(nome)
    pessoa.append(peso)

    if len(registros) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]

    registros.append(pessoa[:])
    pessoa.clear()

    op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op != 'S':
        break

print(f'\nO total de pessoas foi de {len(registros)}')
print(f'A pessoa mais pesada tem {maior}Kg:')
for pessoa in registros:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}...', end='')
print(f'\nA pessoa mais leve tem {menor}Kg:')
for pessoa in registros:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}...', end='')
