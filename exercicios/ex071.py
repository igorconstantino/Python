dinheiro = int(input('Quantos reais deseja sacar? '))

montante = dinheiro
maior_cedula = 50
total_cedulas = 0

while True:
    if montante >= maior_cedula:
        montante -= maior_cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de {maior_cedula}')

        if maior_cedula == 50:
            maior_cedula = 20
        elif maior_cedula == 20:
            maior_cedula = 10
        elif maior_cedula == 10:
            maior_cedula = 1

        total_cedulas = 0

        if total_cedulas == 0:
            break
