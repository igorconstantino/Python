def fatorial(num, show=False):
    """
    -> this function calculates factorial of 'num', showing or not the entire calculus.
    :param num: number that factorial will be calculated.
    :param show: (opcional) determines if the whole account will be showed.
    :return: there is not return.
    """
    if show:
        print(f'{num} x ', end='')
        for i in range(num - 1, 0, -1):
            if i == 1:
                print(f'{i} = ', end='')
                print(num)
            else:
                print(f'{i} x ', end='')
            num *= i
    else:
        for i in range(num - 1, 0, -1):
            num *= i
        print(num)


fatorial(6, True)
print('_' * 50)
help(fatorial)
