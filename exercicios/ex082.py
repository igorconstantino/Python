numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break

print(f'\nA lista completa é: {numeros}')
print(f'Os números pares são: {pares}')
print(f'Os ímpares são: {impares}')
