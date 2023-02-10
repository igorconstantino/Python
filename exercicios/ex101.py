from datetime import date


def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return 'Voto negado'
    elif idade < 18:
        return 'Voto opcional'
    elif idade < 60:
        return 'Voto obrigatório'
    else:
        return 'Voto opcional'


ano_nasc = int(input('Digite o ano de seu nascimento: '))
print(voto(ano_nasc))
