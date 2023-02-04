media = 0
total_idade = 0
TOTAL_PESSOAS = 4
maior_idade = 0
nome_mais_velho = ''
contador_mulheres = 0

for i in range(1, 5):
    nome = input(f'Digite o nome da pessoa {i}: ').strip().capitalize()
    idade = int(input(f'Digite a idade da pessoa {i}: '))
    sexo = input(f'Digite o sexo da pessoa {i}[M/F]: ').strip().upper()

    total_idade += idade

    if i == 1 and sexo in 'M':
        maior_idade = idade
        nome_mais_velho = nome
    else:
        if idade > maior_idade and sexo in 'M':
            maior_idade = idade
            nome_mais_velho = nome

    if sexo in 'F' and idade < 20:
        contador_mulheres += 1

media = total_idade / TOTAL_PESSOAS

print(f'\nA média de idade do grupo é {media}')
print(f'O nome do homem mais velho do grupo é {nome_mais_velho} com {maior_idade} anos')
print(f'A quantidade de mulheres com menos de 20 anos é {contador_mulheres}')
