km = float(input('Digite a distância da sua viagem em km: '))

if km <= 200:
    print('O valor da sua passagem é R${:.2f}'.format(km * 0.50))
else:
    print('O valor da sua passagem é R${:.2f}'.format(km * 0.45))
