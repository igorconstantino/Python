soma = contador = 0

while True:
    num = int(input('Digite um número (999 pra parar): '))

    if num == 999:
        break

    contador += 1
    soma += num

print(f'A soma dos {contador} números foi {soma}')
