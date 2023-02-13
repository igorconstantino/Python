def aumentar(valor, taxa, formatar=False):
    aumento = valor * (taxa / 100)
    valor = valor + aumento

    if formatar:
        str_valor = str(valor)
        str_valor = 'R$' + str_valor
        str_valor = str_valor.replace('.', ',')

        return str_valor
    else:
        return valor


def diminuir(valor, taxa, formatar=False):
    decrescimo = valor * (taxa / 100)
    valor = valor - decrescimo

    if formatar:
        str_valor = str(valor)
        str_valor = 'R$' + str_valor
        str_valor = str_valor.replace('.', ',')

        return str_valor
    else:
        return valor


def dobro(valor, formatar=False):
    valor = valor * 2

    if formatar:
        str_valor = str(valor)
        str_valor = 'R$' + str_valor
        str_valor = str_valor.replace('.', ',')

        return str_valor
    else:
        return valor


def metade(valor, formatar=False):
    valor = valor / 2

    if formatar:
        str_valor = str(valor)
        str_valor = 'R$' + str_valor
        str_valor = str_valor.replace('.', ',')

        return str_valor
    else:
        return valor
