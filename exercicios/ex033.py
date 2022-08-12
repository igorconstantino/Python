num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

maior = num1
if num2 > num1:
    maior = num2
    if num3 > num2:
        maior = num3
elif num3 > num1:
    maior = num3

print('O maior valor é: ', maior)
