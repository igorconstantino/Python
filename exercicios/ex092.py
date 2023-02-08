from datetime import date

pessoa = {'Nome': input('Digite seu nome: ').strip().title(),
          'Ano de nascimento': int(input('Digite o ano de seu nascimento: ')),
          'CTPS': input('Digite sua CTPS: ').strip()}

pessoa['Idade'] = date.today().year - pessoa['Ano de nascimento']
del pessoa['Ano de nascimento']

if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Digite o ano da sua contratação: '))
    pessoa['Salário'] = float(input('Digite seu salário: '))

    print('_' * 50)
    print(f'Nome do(a) contribuinte: {pessoa["Nome"]}')
    print(f'Idade do(a) contribuinte: {pessoa["Idade"]}')
    print(f'Se aposentará com {pessoa["Idade"] + 35} anos')
    print(f'Seu CTPS é {pessoa["CTPS"]} e ganha R${pessoa["Salário"]:.2f}')
