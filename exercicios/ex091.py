from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}

ranking = []

for chave, valor in jogo.items():
    print(f'O {chave} jogou: {valor}')
    sleep(0.5)

print('\n======= RANKING =======')
# (pegando as chaves e valores de jogo, ordenando pelo valor, ordem decrescente)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, valor in enumerate(ranking):
    print(f'{i + 1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(0.5)
