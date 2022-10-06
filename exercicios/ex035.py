l1 = int(input('Digite o valor do lado: '))
l2 = int(input('Digite o valor do lado: '))
l3 = int(input('Digite o valor do lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo')
