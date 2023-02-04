from datetime import date

ano_atual = date.today().year
contador = 0

for i in range(0, 7):
    ano_nasc = int(input('Qual ano você nasceu: '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        contador += 1

print(contador)
