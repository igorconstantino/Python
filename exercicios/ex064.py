contador = 0
soma = 0

num = int(input('Digite um número: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número: '))

print(f'Você digitou {contador - 1} números e a soma entre eles é {soma}')
