l1 = int(input('Digite o valor do lado: '))
l2 = int(input('Digite o valor do lado: '))
l3 = int(input('Digite o valor do lado: '))

if l1 > abs(l2 - l3) and l1 < l2 + l3:
    print('É possivel formar um triângulo!')
if l2 > abs(l1 - l3) and l2 < l1 + l3:
    print('É possivel formar um triângulo!')
if l3 > abs(l2 - l1) and l3 < l2 + l1:
    print('É possivel formar um triângulo!')
