precos = ('PlayStation 5', 4500.00, 'Notebook Acer', 3500.00, 'IPhone 12 Plus', 5000.00, 'Xbox Series S', 3200.00,
          'Cabo USB-C', 100.00)

print('-' * 48)
print('{:^45}'.format('LISTA DE PREÇOS'))
print('-' * 48)

for i in range(0, len(precos), 2):
    print('{:.<35}  R$ {:>.2f}'.format(precos[i], precos[i + 1]))

print('-' * 48)
