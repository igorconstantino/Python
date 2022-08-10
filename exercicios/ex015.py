dias = int(input('Quantos dias foi alugado o carro?'))
km = float(input('Quantos km foram rodados?'))
preco = (60 * dias) + (0.15 * km)
print('O total a pagar pelo aluguel é R${:.2f}'.format(preco))
