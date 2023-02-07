numeros = []

for i in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f'\nO maior valor digitado foi {maior} em: ', end='')
for i, numero in enumerate(numeros):
    if numero == maior:
        print(f'{i}...', end='')

print(f'\nO menor valor digitado foi {menor} em: ', end='')
for i, numero in enumerate(numeros):
    if numero == menor:
        print(f'{i}...', end='')
