def aumentar(valor, taxa):
    aumento = valor * (taxa / 100)
    valor = valor + aumento

    return moeda(valor)


def diminuir(valor, taxa):
    decrescimo = valor * (taxa / 100)
    valor = valor - decrescimo

    return moeda(valor)


def dobro(valor):
    valor = valor * 2

    return moeda(valor)


def metade(valor):
    valor = valor / 2

    return moeda(valor)


def moeda(valor):
    str_valor = str(valor)
    str_valor = 'R$' + str_valor
    str_valor = str_valor.replace('.', ',')

    return str_valor


def resumo(valor, aumento, decrescimo):
    print(f'\n{"TABELA DE PREÇOS":^50}')
    print('-' * 50)
    print(f'{"Valor aumentado: "} \t\t\t\t{aumentar(valor, aumento)}')
    print(f'{"Valor diminuído: "} \t\t\t\t{aumentar(valor, aumento)}')
    print(f'{"Valor dobrado: "} \t\t\t\t{dobro(valor)}')
    print(f'{"Valor dividido por 2: "} \t\t\t{metade(valor)}')
    print('-' * 50)
