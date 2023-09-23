import re
import sys

# Podemos usar o método replace() para substituir os pontos e traços por '' 

entrada = input('Digite um cpf: ') #746.824.890-70
cpf_user = re.sub(r'[^0-9]', '', entrada)

entrada_sequencial = True if entrada[0] * len(entrada) == entrada else False

if entrada_sequencial:
    print('Você digitou dados sequenciais :(')
    sys.exit()

# variáveis
nove_primeiros = cpf_user[:9]
contador = 10
contador2 = 11
soma = 0
soma2 = 0
segundo_val = 0
segundo_val = 0


for digito in nove_primeiros:
    digito = int(digito)

    soma += digito * contador

    contador -= 1

resultado = (soma * 10) % 11

if resultado > 9:
    segundo_val = 0
else:
    segundo_val = resultado


###################################

dez_primeiros = cpf_user[:10]

for digito in dez_primeiros:
    digito = int(digito)

    soma2 += digito * contador

    contador2 -= 1

resultado2 = (soma2 * 10) % 11

if resultado2 > 9:
    segundo_val = 0
else:
    segundo_val = resultado2


###################################

cpf_gerado = f'{nove_primeiros}{resultado}{resultado2}'

if cpf_gerado == cpf_user:
    print('CPF válido.')
else:
    print('CPF inválido!')
