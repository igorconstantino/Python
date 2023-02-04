num1 = int(input('Digite o numero 1:'))
num2 = int(input('Digite o numero 2:'))

if num1 > num2:
    print('O maior número é o {}'.format(num1))
elif num2 > num1:
    print('O maior número é o {}'.format(num2))
else:
    print('\nOs dois são iguais')
