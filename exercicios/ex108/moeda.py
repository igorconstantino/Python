def aumentar(valor, taxa):
    aumento = valor * (taxa / 100)
    return valor + aumento


def diminuir(valor, taxa):
    decrescimo = valor * (taxa / 100)
    return valor - decrescimo


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moeda(valor):
    str_valor = str(valor)
    str_valor = 'R$' + str_valor
    str_valor = str_valor.replace('.', ',')

    return str_valor
