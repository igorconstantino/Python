import moeda as md

valor = float(input('Digite o valor do produto: '))
taxa = int(input('Digite a taxa para aumentar e diminuir o valor: '))

valor_aumentado = md.aumentar(valor, taxa)
valor_diminuido = md.diminuir(valor, taxa)
valor_dobro = md.dobro(valor)
valor_metade = md.metade(valor)

print(f'\nValor aumentado em {taxa}%: {valor_aumentado:.2f}'
      f'\nValor diminuído em {taxa}%: {valor_diminuido:.2f}'
      f'\nValor dobrado: {valor_dobro}'
      f'\nValor dividido em 2: {valor_metade}')
