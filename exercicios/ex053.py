frase = input('Digite uma frase para verificar se é palíndromo: ')  # apos a sopa
frase = frase.replace(' ', '')  # aposasopa

if frase == frase[::-1]:
    print('PALÍNDROMO!!!')
else:
    print('Não é palíndromo!')
