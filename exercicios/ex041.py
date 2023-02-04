from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Você é um nadador mirim.')
elif idade <= 14:
    print('Você é um nadador infantil.')
elif idade <= 19:
    print('Você é um nadador sênior.')
else:
    print('Você é um nadador master.')
