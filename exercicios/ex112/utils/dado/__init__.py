def leia_dinheiro(mensagem):
    valido = False
    while not valido:
        valor = input(mensagem).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print('Erro! ', end='')
        else:
            valido = True
            return float(valor)
