num = int(input('Digite um número: '))
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1

if flag == 1:
    print('Número não é primo!')
else:
    print('Número primo!')
