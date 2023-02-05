cont_maior_18 = 0
cont_homens = 0
cont_mulheres_menor_20 = 0

while True:
    idade = int(input('\nDigite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]

    op = input('Você quer continuar [S/N]? ').strip().upper()[0]

    if idade > 18:
        cont_maior_18 += 1

    if sexo in 'M':
        cont_homens += 1

    if sexo in 'F' and idade < 20:
        cont_mulheres_menor_20 += 1

    if op == 'N':
        break

print(f'\nA quatidade de pessoas maiores de 18 anos foi {cont_maior_18}')
print(f'A quantidade de homens registrados foi {cont_homens}')
print(f'A quantidade de mulheres registradas com menos de 20 anos foi {cont_mulheres_menor_20}')
