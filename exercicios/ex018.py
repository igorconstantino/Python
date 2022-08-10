import math
angulo = float(input('Informe o valor do ângulo: '))
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
print('O valor do cos é {:.2f} e do sen é {:.2f}'.format(cos, sen))
