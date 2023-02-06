num_extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num_user = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num_user >= 20:
        break

print(f'Você digitou o {num_extensos[num_user]}')
