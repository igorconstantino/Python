import moeda as md

valor = float(input('Digite o valor do produto: '))
taxa = int(input('Digite a taxa para aumentar e diminuir o valor: '))
formatar = input('Deseja formatar a moeda? [S/N]').strip().upper()[0]

if formatar == 'S':
    formatar = True
else:
    formatar = False

valor_aumentado = md.aumentar(valor, taxa, formatar)
valor_diminuido = md.diminuir(valor, taxa, formatar)
valor_dobro = md.dobro(valor, formatar)
valor_metade = md.metade(valor, formatar)

print(f'\nValor aumentado em {taxa}%: {valor_aumentado}'
      f'\nValor diminuído em {taxa}%: {valor_diminuido}'
      f'\nValor dobrado: {valor_dobro}'
      f'\nValor dividido em 2: {valor_metade}')
