valorCasa = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salario?'))
anos = int(input('Em quantos anos pretende pagar?'))

prestacao = valorCasa / (anos * 12)

print('\nO valor da prestação é: R${:.2f}'.format(prestacao))

if prestacao > salario * 1.3:
    print('\nDesculpe, você não pode pagar a casa!')
else:
    print('\nParabéns, você pode comprar a casa!')
