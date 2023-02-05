op = 0

num1 = int(input('Digite o valor 1:'))
num2 = int(input('Digite o valor 2:'))

while op != 5:
    print("""
====== MENU ======
(1) - Somar 
(2) - Multiplicar
(3) - Maior
(4) - Novos números
(5) - Sair do programa
==================
    """)
    op = int(input())

    if op == 1:
        print(f'A soma dos números é {num1 + num2}')
    if op == 2:
        print(f'A multiplicação entre os números é {num1 * num2}')
    if op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior entre eles é {maior}')
    if op == 4:
        num1 = int(input('Digite o valor 1:'))
        num2 = int(input('Digite o valor 2:'))
    if op > 5 or op < 1:
        print('OPCÇÃO INVÁLIDA!')
