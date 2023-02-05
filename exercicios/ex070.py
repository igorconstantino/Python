total_gasto = 0
cont_maior_1000 = 0
produto_menor_preco = 0
cont_produtos = 0
nome_menor_preco = ''

while True:
    nome = input('\nDigite o nome do produto: ').strip()
    preco = float(input('Digite o preço do produto: '))
    print('-' * 25)
    op = input('Você quer continuar [S/N]? ').strip().upper()[0]

    cont_produtos += 1

    total_gasto += preco

    if preco > 1000:
        cont_maior_1000 += 1

    if cont_produtos == 1:
        nome_menor_preco = nome
        produto_menor_preco = preco
    else:
        if preco < produto_menor_preco:
            produto_menor_preco = preco
            nome_menor_preco = nome

    if op == 'N':
        break

print(f'\nO total gasto foi de R${total_gasto:.2f}')
print(f'A quantidade de produtos maior que R$1000.00 foi de {cont_maior_1000}')
print(f'O produto com menor preço foi  {nome_menor_preco} custando R${produto_menor_preco:.2f}')
