jogador = {'Nome': input('Qual o nome do jogador?: ').strip().title(),
           'Gols': [],
           'Total': 0}

qtd_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))

for i in range(qtd_partidas):
    gols = int(input(f'Quantos gols fez na {i + 1}ª partida?: '))
    jogador['Gols'].append(gols)
    jogador['Total'] += gols

print('_' * 50)
print(jogador)

print('_' * 50)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem valor {valor}.')

print('_' * 50)
print(f'O jogador {jogador["Nome"]} jogou {qtd_partidas} partidas.')
for i in range(qtd_partidas):
    print(f'\t=> Na partida {i + 1}, fez {jogador["Gols"][i]} gols')

print(f'Foi um total de {jogador["Total"]} gols.')
