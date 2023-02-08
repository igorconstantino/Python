# pessoa = [{'nome': 'Igor', 'idade': 20, 'sexo': 'M'}, {'nome': 'Thamires', 'idade': 22, 'sexo': 'F'}]

pessoas = []
pessoa = {}
soma_idades = 0

while True:
    nome = input('Digite o nome da pessoa: ').strip().title()
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('ÍNVALIDO! Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
    idade = int(input('Digite a idade da pessoa: '))

    soma_idades += idade

    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade

    pessoas.append(pessoa.copy())

    op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while op not in 'SN':
        op = input('ÍNVALIDO! Deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break

print('_' * 50)
print(f'A) O total de pessoas cadastradas é {len(pessoas)}.')
print(f'B) A média de idade é {soma_idades / len(pessoas)}.')
print('C) As mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=', ')
print('\nD) Lista das pessoas que estão acima da média de idade: ')
for pessoa in pessoas:
    if pessoa['idade'] > (soma_idades / len(pessoas)):
        print(f'\tNome = {pessoa["nome"]}; Idade = {pessoa["idade"]}; Sexo = {pessoa["sexo"]}')
