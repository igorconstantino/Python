from datetime import date
anoAtual = date.today().year

anoNasc = int(input('Digite o ano de seu nascimento: '))
idade = anoAtual - anoNasc

if idade < 18:
    print('Ainda não chegou sua hora de se alistar, ainda faltam {} anos!'.format(18 - idade))
elif idade > 18:
    print('Já passou da hora de você se alistar, se passaram {} anos!'.format(idade - 18))
else:
    print('É hora de você se alistar!')
