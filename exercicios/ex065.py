op = 's'
soma = 0
contador_num = 0
maior = menor = 0

while op == 's':
    num = int(input('Digite um número inteiro: '))

    soma += num
    contador_num += 1

    if contador_num == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
    
    op = input('Você quer continuar? [s/n]: ')

media = soma / contador_num

print(f'A média dos números é {media} e o menor número é {menor}')
