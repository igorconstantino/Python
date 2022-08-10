import math
catetoOp = float(input('Informe o comprimento do cateto oposto: '))
catetoAd = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(catetoOp, 2) + math.pow(catetoAd, 2))
print('A hipotenusa vale {:.2f}'.format(hipotenusa))
