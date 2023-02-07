parenteses = []

expressao = input('Digite uma expressão com parênteses: ').strip()

for letra in expressao:
    if letra in '()':
        parenteses.append(letra)

abre_parenteses = parenteses.count('(')
fecha_parenteses = parenteses.count(')')

if abre_parenteses == fecha_parenteses:
    print('Expressão válida!!!')
else:
    print('Expressão inválida!!!')
