numeros = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    op = input('Você deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break

numeros.sort(reverse=True)

print(f'\nForam digitados {len(numeros)} valores')
print(f'A lista em ordem descrescente é {numeros}')
if 5 in numeros:
    print('O valor 5 foi encontrado!')
else:
    print('O valor 5 não foi encontrado!')
    