velCarro = float(input('Digite a valocidade do carro: '))

if velCarro > 80:
    print('Você foi multado!')
    print('Sua multa será de R${:.2f}'.format((velCarro - 80) * 7))

print('Tenha um bom dia, dirija com segurança.')
