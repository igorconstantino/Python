fatorial = 1

num = int(input('Digite um número para calcular o fatorial: '))
num_aux = num

while num > 0:
    fatorial *= num
    num -= 1

print(f'O fatorial de {num_aux} é {fatorial}')
