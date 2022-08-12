salario = float(input('Digite seu salrio: '))
if salario > 1250:
    print('Seu novo salário é R${:.2f}'.format(salario + (salario * 10/100)))
else:
    print('Seu novo salário é R${:.2f}'.format(salario + (salario * 15/100)))
