l1 = int(input('Digite o valor do lado 1: '))
l2 = int(input('Digite o valor do lado 2: '))
l3 = int(input('Digite o valor do lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: # é possivel formar triangulo
    if l1 == l2 and l2 == l3:
        print('Formará um triangulo equilatero!')
    elif (l1 == l2 and l2 != l3) or (l1 == l3 and l3 != l2) or (l2 == l3 and l3 != l1):
        print('Formará um triangulo isósceles!')
    else:
        print('Formarà um triangulo escaleno!')
else:
    print('Não é possivel formar um triângulo')
