op = 's'
soma = 0
contador_num = 0
menor = 999999

while op == 's':
    num = int(input('Digite um número inteiro: '))

    if num < menor:
        menor = num

    soma += num
    contador_num += 1

    op = input('Você quer continuar? [s/n]: ')

media = soma / contador_num

print(f'A média dos números é {media} e o menor número é {menor}')
