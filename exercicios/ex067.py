while True:
    num = int(input('\nDigite o número referente a tabuada desejada: '))

    if num < 0:
        print('Obrigado por utilizar nosso programa!')
        break

    for i in range(0, 11):
        print(f'{num} X {i} = {num * i}')