def ficha(nome='', gols=0):
    print(f'O jogador {nome} marcou {gols} gols')


nome_ = input('Informe o nome do jogador: ').strip().title()
gols_ = input('Informe quantos gols ele marcou: ')

if nome_ == '':
    nome_ = '<desconhecido>'

if gols_.isnumeric():
    gols_ = int(gols_)
else:
    gols_ = 0
ficha(nome_, gols_)
