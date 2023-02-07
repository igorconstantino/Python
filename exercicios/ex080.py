numeros = []

for i in range(5):
    num = int(input('Digite um número: '))
    if i == 0 or num > max(numeros):
        numeros.append(num)
        print('Valor inserido no final')
    else:
        j = 0
        while j < len(numeros):
            if num <= numeros[j]:
                numeros.insert(j, num)
                break
            j += 1

print(f'Lista ordenada: {numeros}')
