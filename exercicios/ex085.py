lista = [[], []]

for i in range(7):
    num = int(input(f'Digite o {i + 1}° número: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Valores pares em ordem: {lista[0]}')
print(f'Valores ímpares em ordem: {lista[1]}')
