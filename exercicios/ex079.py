numeros = []

while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Valor duplicado, não foi adicionado!')

    op = input('Você deseja continuar? [S/N]: ').strip().upper()[0]
    if op != 'S':
        break
        
numeros.sort()
print(f'Os valores em ordem crescente são: {numeros}')
